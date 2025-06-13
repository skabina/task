import json
import os
import asyncio
from dotenv import load_dotenv
from telethon import TelegramClient
from datetime import datetime, timedelta, timezone
from telethon.errors import FloodWaitError
from config import api_id, api_hash
import logging

logging.basicConfig(level = logging.DEBUG)


one_month_ago = datetime.now(timezone.utc) - timedelta(days=1)  



class TelegramAccount():
    def __init__ (self, ):
        self.client = TelegramClient('date', api_id, api_hash)

    def start(self):
        return self.client.start()
    
    def disconnect(self):
        return self.client.disconnect()

    async def get_date(self):
        chats_data = []

        async for dialog in self.client.iter_dialogs(limit=10):
            chat_info = {
                "chat_id": dialog.id, 
                "chat_name": dialog.name, 
                "messages": []
            }

            if dialog.is_group or dialog.is_user:
                logging.info( u'Everything is cool')
                
                messages = []
                async for message in self.client.iter_messages(dialog.id):
                    if message.date < one_month_ago:
                        logging.info(f"Skipping message from {message.date} as it is older than one month.")
                        break
                    if message.text:
                        sender = await self.client.get_entity(message.sender_id)
                        sender_name = sender.username if sender.username else str(sender.id)
                        msg_time = message.date.astimezone(timezone.utc).strftime("%H:%M")
                        messages.append({"date": message.date, "text": f"{sender_name} [{msg_time}]: {message.text[:50]}"})

                            
                messages.sort(key=lambda x: x["date"])    
                chat_info["messages"] = [msg["text"] for msg in messages]

                if chat_info["messages"]: 
                    chats_data.append(chat_info)         
            else:
                logging.info(f"Skipping non-user chat: {dialog.name} (ID: {dialog.id})")
    
        with open('chats_data.json', 'w', encoding='utf-8') as json_file:
            json.dump(chats_data, json_file, ensure_ascii=False, indent=4)
        logging.info(f"Saved {len(chats_data)} chats to 'chats_data.json'.")
