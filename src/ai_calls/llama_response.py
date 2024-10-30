from tools import Quran_recite, Quran_recite_tool, record_audio_tool, manage_recordings_tool
from icecream import ic
import json 

def llama_response(chat_messages: list, saved_recordings: list, client) -> tuple[str, list, int, list, bool, str, list, list, list]:
    """Generate a response from the Llama model and return the text response, the audio urls, the arabic ayat list and the updated chat_messages"""
    
    filtered_chat_messages = [msg for msg in chat_messages if isinstance(msg.get('content'), str)]

    
    response = client.chat.completions.create(
            messages=filtered_chat_messages,
            model="llama-3.1-70b-versatile",
            tools=[Quran_recite_tool, record_audio_tool, manage_recordings_tool],
            tool_choice="auto"
    )


    text_response = response.choices[0].message.content
    tool_calls = response.choices[0].message.tool_calls


    if tool_calls:
        available_functions = {
            "Quran_recite": Quran_recite,
            "record_audio": 'record_audio',
            "manage_recordings": 'manage_recordings'
        }

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            
            
            if function_name == "record_audio":
                is_record = True
                chat_messages.append({
                    "role": "tool",
                    "name": function_name,
                    "message": function_args.get("message"),
                    "record_label": function_args.get("record_label"),
            })
                return (function_args.get("message"),
                        [], 
                        0, 
                        [], 
                        is_record, 
                        function_args.get("record_label"), 
                        chat_messages,
                        [],
                        [])
            
            
            elif function_name == "manage_recordings":
                chat_messages.append({
                    "role": "tool",
                    "name": function_name,
                    "message": function_args.get("message"),
                    "displayed_recordings": function_args.get("recordings_to_display"),
                    "deleted_recordings": function_args.get("recordings_to_delete"),
                })
                return (function_args.get("message"),
                        [], 
                        0, 
                        [], 
                        False, 
                        "empty", 
                        chat_messages,
                        function_args.get("recordings_to_display"),
                        function_args.get("recordings_to_delete"))
            
            elif function_name == "Quran_recite":
                audio_urls, arabic_ayat_list = function_to_call(
                    surah_number=int(function_args.get("surah_number")),
                    verses_to_recite=function_args.get("verses_to_recite")
            )

                chat_messages.append({
                    "role": "tool",
                    "name": function_name,
                    "surah_number": function_args.get("surah_number"),
                    "verses_to_recite": function_args.get("verses_to_recite"),
                    "content": "You succesfully recited the ayah/verse from the Quran",
                })
                
                return (function_args.get("message"),
                        audio_urls,
                        int(function_args.get("repeat_number")),
                        arabic_ayat_list,
                        False,
                        "empty",
                        chat_messages,
                        [],
                        [])


    chat_messages.append({
        "role": "assistant",
        "content": text_response,
    })
    
    return (text_response,
            [],
            0,
            [],
            False,
            "empty",
            chat_messages,
            [],
            [])

if __name__ == "__main__":

    chat_messages = [
        {"role": "user", "content": "Can I see all my recordings?"}
    ]
    from groq import Groq
    client = Groq(api_key="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")
    response, audio_urls, repeat_number , arabic_ayat_list, is_record, record_label, updated_chat_messages, recordings_to_display, recordings_to_delete = llama_response(chat_messages, [], client)
    ic(response)
    ic(audio_urls)
    ic(arabic_ayat_list)
    ic(recordings_to_display)
    ic(recordings_to_delete)