import json
import os
from dotenv import load_dotenv
from telethon import TelegramClient
from datetime import datetime, timedelta, timezone

load_dotenv()


api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')


client = TelegramClient('date', api_id, api_hash)


one_month_ago = datetime.now(timezone.utc) - timedelta(days=1)  


async def get_Date(client):
 
    chats_data = []
    
    async for dialog in client.iter_dialogs(limit=10):
        chat_info = {"chat_id": dialog.id, "chat_name": dialog.name, "messages": []}

        if dialog.is_group or dialog.is_user:
            print(f"\nЧат: {dialog.name} — ID: {dialog.id}")
            
            
            async for message in client.iter_messages(dialog.id):
                if message.date < one_month_ago:
                    break  
                if message.text:
                    sender = await client.get_entity(message.sender_id)
                    sender_name = sender.username if sender.username else str(sender.id)
                    chat_info["messages"].append(f"{sender_name}: {message.text[:50]}")
                    chats_data.append(chat_info)

        else:
            print(f"\nПропускаємо канал: {dialog.name} — ID: {dialog.id}")
            
    with open('chats_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(chats_data, json_file, ensure_ascii=False, indent=4)
