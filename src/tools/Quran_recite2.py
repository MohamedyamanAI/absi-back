from pydub import AudioSegment
from icecream import ic
from .get_ayat import get_ayat
import os , base64, pygame, json


def Quran_recite(surah_number: int, verses_to_recite: list) -> tuple[list, list]:
    """Recite specific verses from a specific surah from the Quran"""

    try:
        # Convert string representation of list to actual list of integers
        if isinstance(verses_to_recite, str):
            # Remove brackets and split by commas
            verses_to_recite = [int(x.strip()) for x in verses_to_recite.strip('[]').split(',')]
        # If already a list, ensure all elements are integers
        else:
            verses_to_recite = [int(x) for x in verses_to_recite]

        current_dir = os.path.dirname(os.path.abspath(__file__))
        # json_file = os.path.join(current_dir, 'AbdulBaset AbdulSamad Recitation.json')
        json_file = os.path.join(current_dir, 'Hani ar-Rifai Recitation.json')

        if not os.path.exists(json_file):
            raise FileNotFoundError(f"The JSON file {json_file} does not exist.")
            
        with open(json_file, 'r', encoding='utf-8') as f:
            recitation_data = json.loads(f.read())

        # Get matching ayat using get_ayat function
        ic(surah_number, verses_to_recite)
        matching_ayat = get_ayat(surah_number, verses_to_recite, recitation_data)
        ic(matching_ayat)
        # Just return the URLs and Arabic text if available
        audio_urls = [ayah['audio_url'] for ayah in matching_ayat]
        arabic_ayat_list = []
        for ayah in matching_ayat:
            if 'arabic_text' in ayah:
                arabic_ayat_list.append(ayah['arabic_text'])
        
        return audio_urls, arabic_ayat_list
    except Exception as e:
        import traceback
        error_traceback = traceback.format_exc()
        return [f"An error occurred: {str(e)}\n\nTraceback:\n{error_traceback}"], []
    finally:
        pygame.mixer.quit()


if __name__ == "__main__":
    audio_urls, arabic_ayat_list = Quran_recite(2, [1])
    print(audio_urls)
    print(arabic_ayat_list)
    
