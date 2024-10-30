def get_surah_number(surah_number_or_name: str) -> int:
    """Get the surah number"""
    surah_names = {
        'Al-Fatihah': 1,
        'Al-Baqarah': 2,
        'Al-Imran': 3,
        'An-Nisa': 4,
        'Al-Maida': 5,
        'Al-Anam': 6,
        'Al-Araf': 7,
        'Al-Anfal': 8,
        'At-Tawbah': 9,
        'Yunus': 10
    }
    
    if surah_number_or_name.lower().startswith('a'):
        surah_number = surah_names.get(surah_number_or_name,1)
        return surah_number
    else:
        return int(surah_number_or_name)