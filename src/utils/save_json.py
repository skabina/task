import json


def save_json(date):
    with open('chats.json', 'w', encoding='utf-8') as f:
        json.dump(date, f, ensure_ascii=False, indent=4)