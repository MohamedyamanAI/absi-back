record_audio_tool = {
    "type": "function",
    "function": {
        "name": "record_audio",
        "description": "Record the audio of the kid reciting Quran",
        "parameters": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "A normal message from the kid, like: Ok! lets start, or go ahead!",
                },
                "record_label": {
                    "type": "string",
                    "description": "What the kid will recite, like: AL-Fatiha verses 1-5, AL-Baqarah verses 3-7, etc.",
                }
            },
            "required": ["message", "record_label"],
        }
    }
}
