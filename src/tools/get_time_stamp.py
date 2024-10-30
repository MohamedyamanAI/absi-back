from .ayat_time_stamps.surah001 import surah001


def get_time_stamp(start_verse_number: int) -> int:
    """Get the time stamps of the verses/ayat in a specific surah"""

    return surah001[int(start_verse_number) - 1]