from .arabic_ayat import surah001_ayat

def get_arabic_ayat(start_verse_number: int, number_of_verses: int) -> list:
    """Get the Arabic ayat from a specific verse/verses"""
    
    return surah001_ayat[int(start_verse_number) -1 :int(start_verse_number)+int(number_of_verses) -1 ]