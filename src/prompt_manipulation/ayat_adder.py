from prompts import Al_Fatiha_surah, Al_Baqarah_surah

def ayat_adder(conversation_history : list, transcription : str, prev_mentions : list = []) -> tuple:
    
    mention = []
    
    if "quran" in transcription.lower() or "fatiha" in transcription.lower():
        conversation_history[0]["content"] += Al_Fatiha_surah if Al_Fatiha_surah not in mention else None

    if "quran" in transcription.lower() or "baqarah" in transcription.lower():
        conversation_history[0]["content"] += Al_Baqarah_surah if Al_Baqarah_surah not in mention else None

    if "continue" in transcription.lower() or "more" in transcription.lower():
        conversation_history[0]["content"] += mention

    return conversation_history, mention
