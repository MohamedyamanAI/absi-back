Quran_recite_tool = {
    "type": "function",
    "function": {
        "name": "Quran_recite",
        "description": "Recite a specific verse/verses from a specific surah from the Quran, use this tool once to recite all the verses if more than one",
        "parameters": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "A message before reciting the verses, like Ok!, lets start, lets listen together, etc.",
                },
                "surah_number": {
                    "type": "string",
                    "description": "The surah number that you want to recite",
                },
                "verses_to_recite": {
                    "type": "array",
                    "description": "A list of verses/ayat numbers that you will recite.",
                    "items": {
                        "type": "integer",
                        "description": "The verse/ayah number that you will recite.",
                    }
                },
                "repeat_number": {
                    "type": "integer",
                    "description": "The number of times you want to repeat the verses, always one unless the kid state otherwise",
                }
            },
            "required": ["surah_number", "verses_to_recite","message", "repeat_number"],
        }
    }
}

# Quran_recite_tool = {
#     "type": "function",
#     "function": {
#         "name": "Quran_recite",
#         "description": "Recite a specific verse/verses from a specific surah from the Quran, use this tool once to recite all the verses if more than one",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "surah_number_or_name": {
#                     "type": "string",
#                     "description": "The surah number or name that you want to recite",
#                     "enum": ['1','2','3','4','5', 'Al-Fatihah', 'Al-Baqarah', 'Al-Imran', 'An-Nisa', 'Al-Maida']
#                 },
#                 "start_verse_number": {
#                     "type": "integer",
#                     "description": "The verse/ayah number that you will start reciting from.",
#                 },
#                 "number_of_verses": {
#                     "type": "integer",
#                     "description": "The number of verse/ayah to recite, if the user wants to recite the whole surah choose 999",
#                 }
#             },
#             "required": ["surah_number_or_name", "start_verse_number", "number_of_verses"],
#         }
#     }
# }
