from pydub import AudioSegment
from icecream import ic
from .ayat_time_stamps import surah001
import os , base64, pygame
from .get_time_stamp import get_time_stamp
from .get_surah_number import get_surah_number
from .get_arabic_ayat import get_arabic_ayat


def Quran_recite(surah_number_or_name: str, start_verse_number: int, number_of_verses: int) -> tuple[list, list]:
    """Recite specific verses from a specific surah from the Quran"""
    
    surah_number = get_surah_number(surah_number_or_name)
    start_verse_time_stamp = get_time_stamp(start_verse_number)
    arabic_ayat_list = get_arabic_ayat(start_verse_number, number_of_verses)
    
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        audio_file = os.path.join(current_dir, 'ayat_time_stamps', f'surah{int(surah_number):03d}.wav')
        
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"The audio file {audio_file} does not exist.")

        audio = AudioSegment.from_wav(audio_file)
        
        surah_timestamps = surah001  # Make sure to use the correct timestamps for the surah
        start_index = surah_timestamps.index(start_verse_time_stamp)
        end_index = min(start_index + int(number_of_verses), len(surah_timestamps))
        
        audio_base64_list = []
        
        for i in range(start_index, end_index):
            verse_start = surah_timestamps[i]
            verse_end = surah_timestamps[i + 1] if i + 1 < len(surah_timestamps) else len(audio)
            
            extracted_audio = audio[verse_start:verse_end]
            
            temp_file = f"temp_recitation_{i}.wav"
            extracted_audio.export(temp_file, format="wav")
            
            with open(temp_file, "rb") as f:
                audio_base64 = base64.b64encode(f.read()).decode('utf-8')
            
            audio_base64_list.append(audio_base64)
            
            try:
                os.remove(temp_file)
            except PermissionError:
                print(f"Warning: Unable to remove temporary file {temp_file}. It may need to be deleted manually.")
        
        return audio_base64_list, arabic_ayat_list
    
    except Exception as e:
        import traceback
        error_traceback = traceback.format_exc()
        return [f"An error occurred: {str(e)}\n\nTraceback:\n{error_traceback}"], []
    finally:
        pygame.mixer.quit()


if __name__ == "__main__":
    audio_base64_list, arabic_ayat_list = Quran_recite("Al-Fatihah", 3, 2)
    
    if not audio_base64_list[0].startswith("An error occurred"):
        for audio_base64 in audio_base64_list:
            audio_data = base64.b64decode(audio_base64)
            temp_file = "temp_recitation.wav"
            with open(temp_file, "wb") as f:
                f.write(audio_data)

            try:
                pygame.mixer.init()
                pygame.mixer.music.load(temp_file)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
            except KeyboardInterrupt:
                print("\nPlayback stopped.")
            finally:
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                pygame.quit()

        try:
            os.remove(temp_file)
        except PermissionError:
            print(f"Warning: Unable to remove temporary file {temp_file}. It may need to be deleted manually.")
    else:
        print(audio_base64_list[0])
