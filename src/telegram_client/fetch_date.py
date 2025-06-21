from datetime import datetime, timedelta, timezone
from typing import List
from models.chat import ChatInfo, ChatMessage
from telethon import TelegramClient
from telegram_client.crud import sort_messages
from utils.save_json import save_json

one_month_ago = datetime.now(timezone.utc) - timedelta(days=30)

async def fetch_date(client: TelegramClient):
    chat_list: List[ChatInfo] = []

    async for dialog in client.iter_dialogs(limit=10):
        if dialog.is_group or dialog.is_user:
            print(f"Обробка чату: {dialog.name} (ID: {dialog.id})")
            content: List[ChatMessage] = []

            async for message in client.iter_messages(dialog.id):
                if message.date < one_month_ago:
                    break


                if message.text:
                    sender = await client.get_entity(message.sender_id)
                    sender_name = sender.username if sender.username else str(sender.id)
                    message_time = message.date.astimezone(timezone.utc).strftime("%H:%M:%S")
                    content.append(ChatMessage(
                        sender=sender_name, 
                        time=message_time, 
                        content=message.text
                        ))
                                 

            if content:
                sorted_content = sort_messages(content)
                chat_info = ChatInfo(
                    chat_id=dialog.id,
                    chat_name=dialog.name,
                    messages=sorted_content
                )
                chat_list.append(chat_info)
                
    return chat_list
    
    
