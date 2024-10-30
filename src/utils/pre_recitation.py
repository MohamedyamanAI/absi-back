import base64
from pydub import AudioSegment
import io

from ai_calls import text_to_speech

def pre_recitation_adder(audio_base64: str) -> str:
    intro_audio_base64 = text_to_speech("Ok, let's listen together!")
    silence = AudioSegment.silent(duration=1000)  # 1 second of silence
    
    # Convert intro_audio from base64 to AudioSegment
    intro_audio = AudioSegment.from_wav(io.BytesIO(base64.b64decode(intro_audio_base64)))
    
    # Decode the base64 Quran recitation
    quran_audio = AudioSegment.from_wav(io.BytesIO(base64.b64decode(audio_base64)))
    
    # Combine intro, silence, and Quran recitation
    combined_audio = intro_audio + silence + quran_audio
    
    # Convert the combined audio back to base64
    buffer = io.BytesIO()
    combined_audio.export(buffer, format="wav")
    audio_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    return audio_base64