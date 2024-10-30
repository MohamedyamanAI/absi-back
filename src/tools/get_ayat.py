def get_ayat(surah_number : int, ayat_list : list, recitation_data : list) -> list:
    """
    Retrieves ayahs from a specific surah based on ayah numbers
    
    Args:
        surah_number (int): The number of the surah
        ayat_list (list): List of ayah numbers to retrieve
        recitation_data (list): List of recitation objects containing surah and ayah data
        
    Returns:
        list: List of matching ayah objects
    """
    matching_ayat = []
    surah_position = 1  # Track position within current surah
    
    if isinstance(recitation_data, dict):
        recitation_data = list(recitation_data.values())
    
    for ayah in recitation_data:
        if ayah["surah_number"] == surah_number:
            if surah_position in ayat_list:
                matching_ayat.append(ayah)
            surah_position += 1
        elif ayah["surah_number"] > surah_number:
            break
            
    return matching_ayat

if __name__ == "__main__":
    get_ayat(1, [1, 2], [])

