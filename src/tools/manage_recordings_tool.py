manage_recordings_tool = {
    "type": "function",
    "function": {
        "name": "manage_recordings",
        "description": "Manage the kid's recitations recordings",
        "parameters": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "A message before displaying or deleting the recordings, like Ok!, here are your recordings, or here are the recordings you want to delete.",
                },
                "recordings_to_display": {
                    "type": "array",
                    "description": "A list of the kid's recitations recordings IDs to display. If you do not need to display any recordings, leave it empty. If the kid asks to display all the recordings, put all the recordings IDs that you have in the list. like: ['192a2082-ac2d-457d-9a94-c2f72c7bf2b3', '7819383c-d339-4ffc-8675-d3b836db3cb2']",
                    "items": {
                        "type": "string",
                        "description": "The kid's recitations recordings ID.",
                    }
                },
                "recordings_to_delete": {
                    "type": "array",
                    "description": "The kid's recitations recordings IDs to delete. like ['192a2082-ac2d-457d-9a94-c2f72c7bf2b3', '7819383c-d339-4ffc-8675-d3b836db3cb2']. Do not delete all the recordings unless the kid asks explisitly for it. If you do not need to delete any recordings, leave it empty.",
                    "items": {
                        "type": "string",
                        "description": "The kid's recitations recordings ID to delete.",
                    }
                }
            }, 
            "required": ["message", "recordings_to_display", "recordings_to_delete"],
        }
    }
}

