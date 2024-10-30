from flask import Flask, request, jsonify
from src import transcribe_audio, llama_response, ayat_adder, default_absi_prompt, text_to_speech, pre_recitation_adder
from flask_cors import CORS
from groq import Groq
from icecream import ic
from pydub import AudioSegment
import os

app = Flask(__name__)
CORS(app, expose_headers=['X-JSON-Response'])  
client = Groq(api_key="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")
model = 'llama3-groq-70b-8192-tool-use-preview'

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400
    
    audio_file = request.files['audio']
    original_filename = "original_audio"
    converted_filename = "audio.wav"
    
    try:
        # Save the original file
        audio_file.save(original_filename)
        
        # Convert to wav using pydub
        audio = AudioSegment.from_file(original_filename)
        # Export as WAV with specific parameters
        audio.export(converted_filename, 
                    format="wav",
                    parameters=["-acodec", "pcm_s16le", 
                              "-ac", "1", 
                              "-ar", "16000"])
        
        # Now transcribe the converted file
        transcription = transcribe_audio(converted_filename, client)
        
        # Clean up files
        if os.path.exists(original_filename):
            os.remove(original_filename)
        if os.path.exists(converted_filename):
            os.remove(converted_filename)
            
        return jsonify({"transcription": transcription.text})
    except Exception as e:
        ic(e)
        # Clean up files in case of error
        if os.path.exists(original_filename):
            os.remove(original_filename)
        if os.path.exists(converted_filename):
            os.remove(converted_filename)
        return jsonify({"error": str(e)}), 500


@app.route('/message', methods=['POST'])
def message():
    data = request.json

    message = data.get('message')
    chat_messages = data.get('chatMessages')
    saved_recordings = data.get('savedRecordings', [])  # Add default empty list
    # ic(saved_recordings)
    
    # Format the recordings in a more readable way
    recordings_text = "\nSaved kid's recitations recordings:\n" + "\n".join([f"- {rec}" for rec in saved_recordings]) if saved_recordings else ""
    
    if not message:
        return jsonify({"error": "No message provided"}), 400
    
    if not any(message["role"] == "system" for message in chat_messages):
        chat_messages.insert(0, {"role": "system", "content": default_absi_prompt + recordings_text})
    else:
        chat_messages[0]["content"] = default_absi_prompt + recordings_text
        
    chat_messages += [{"role": "user", "content": message}]
    
    (text_response,
     audio_urls,
     repeat_number,
     arabic_ayat_list,
     is_record,
     record_label,
     chat_messages,
     recordings_to_display,
     recordings_to_delete) = llama_response(chat_messages, saved_recordings, client)
    
    # ic(text_response, audio_urls, arabic_ayat_list, chat_messages)
    # ic("record_label: ", record_label)
    # ic(message, recordings_to_display, recordings_to_delete)
    
    return jsonify({
        "text_response": text_response,
        "chat_messages": chat_messages,
        "audio_urls": audio_urls,
        "arabic_ayat_list": arabic_ayat_list,
        "is_record": is_record,
        "record_label": record_label,
        "repeat_number": repeat_number,
        "recordings_to_display": recordings_to_display,
        "recordings_to_delete": recordings_to_delete
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
