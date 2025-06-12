import json
import os
import asyncio
from dotenv import load_dotenv
from telethon import TelegramClient
from datetime import datetime, timedelta, timezone
from telethon.errors import FloodWaitError
from config import api_id, api_hash

client = TelegramClient('date', api_id, api_hash)

one_month_ago = datetime.now(timezone.utc) - timedelta(days=30)  # За останній день

async def get_date(client):
    chats_data = []

    async for dialog in client.iter_dialogs(limit=10):
        chat_info = {"chat_id": dialog.id, "chat_name": dialog.name, "messages": []}

        if dialog.is_group or dialog.is_user:
            print(f"\nЧат: {dialog.name} — ID: {dialog.id}")

            messages = []
            async for message in client.iter_messages(dialog.id):
                if message.date < one_month_ago:
                    break
                if message.text:
                    try:
                        sender = await client.get_entity(message.sender_id)
                        sender_name = sender.username if sender.username else str(sender.id)
                        msg_time = message.date.astimezone(timezone.utc).strftime("%H:%M")
                        messages.append({"date": message.date, "text": f"{sender_name} [{msg_time}]: {message.text[:50]}"})
                    except FloodWaitError as e:
                       
                        print(f"FloodWaitError: Очікуємо {e.seconds} секунд.")
                        await asyncio.sleep(e.seconds)  
                        continue  

            messages.sort(key=lambda x: x["date"])    
            chat_info["messages"] = [msg["text"] for msg in messages]

            if chat_info["messages"]: 
                chats_data.append(chat_info)

        else:
            print(f"\nПропускаємо канал: {dialog.name} — ID: {dialog.id}")
   
    with open('chats_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(chats_data, json_file, ensure_ascii=False, indent=4)

async def main():
    await client.start()
    await get_date(client)

if __name__ == "__main__":
    asyncio.run(main())
