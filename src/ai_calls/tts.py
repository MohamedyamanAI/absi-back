import io
import base64
from pydub import AudioSegment
from gtts import gTTS
import pygame 
import os
def text_to_speech(text: str) -> str:
    """
    Convert text to speech and return audio data as base64 encoded string.
    
    Args:
        text (str): The text to be converted to speech.
    
    Returns:
        str: The audio data in base64 encoded WAV format.
    """
    # Create a gTTS object
    tts = gTTS(text=text, lang='en', slow=False)
    
    # Create a BytesIO buffer to store the audio
    audio_buffer = io.BytesIO()
    
    # Save the audio to the buffer
    tts.write_to_fp(audio_buffer)
    
    # Reset the buffer position to the beginning
    audio_buffer.seek(0)
    
    # Convert the MP3 to WAV format
    audio = AudioSegment.from_mp3(audio_buffer)
    output_buffer = io.BytesIO()
    audio.export(output_buffer, format="wav")
    
    # Get the bytes from the output buffer
    audio_data = output_buffer.getvalue()
    
    # Encode the audio data in base64
    audio_base64 = base64.b64encode(audio_data).decode('utf-8')
    
    return audio_base64

if __name__ == "__main__":
    audio_data = text_to_speech("Hello, how are you today?")
    print(f"Audio data length: {len(audio_data)} bytes")
    
    # Decode the base64 audio data
    audio_data_bytes = base64.b64decode(audio_data)
    
    # Play the audio data
    temp_file = "temp_tts.wav"
    with open(temp_file, "wb") as f:
        f.write(audio_data_bytes)

    pygame.mixer.init()
    try:
        pygame.mixer.music.load(temp_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    finally:
        pygame.mixer.quit()  # Ensure pygame releases the file
        pygame.quit()

    try:
        os.remove(temp_file)
    except PermissionError:
        print(f"Unable to remove temporary file: {temp_file}")
