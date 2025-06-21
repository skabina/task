

import json


def sort_messages(chat_list):
    sorted_messages = reversed(chat_list)
    print(f"Sorted {sorted_messages} messages by time.")
    return sorted_messages


def correct_message(chat_list):
    chat_output = []
    for chat in chat_list:
        chat_output.append({
            "chat_id": chat.chat_id,
            "chat_name": chat.chat_name,
            "messages": [
                f"{msg.sender} [{msg.time}]: {msg.content}" 
                for msg in chat.messages
            ]
        })
    print(f"Corrected {len(chat_output)} chats.")
    return chat_output



def save_json(date):
    with open('chats.json', 'w', encoding='utf-8') as f:
        json.dump(date, f, ensure_ascii=False, indent=4)