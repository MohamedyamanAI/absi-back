import os
from groq import Groq


def transcribe_audio(filename : str, client):
    with open(filename, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(filename, file.read()), 
            model="distil-whisper-large-v3-en",
            response_format="json",  
            language="en", 
            temperature=0.0 
        )
    file.close()
    os.remove(filename)
    return transcription

if __name__ == "__main__":
    client = Groq(api_key="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")
    transcription = transcribe_audio("audio.wav", client)
    print(transcription.text)
