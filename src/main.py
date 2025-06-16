import json
import asyncio
from telegram_client.client import get_client
from telegram_client.fetch_date import fetch_date
from ai.ai_connect import ai_connect
from ai.ai_analiz import ai_analiz

async def main():
    
    client = get_client()
    await client.start()

    chat_list = await fetch_date(client)

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

    with open("chats.json", "w", encoding="utf-8") as f:
        json.dump(chat_output, f, indent=2, ensure_ascii=False)

    await client.disconnect()
    

    model = ai_connect()
    with open('chats.json', 'r', encoding='utf-8') as file:
        chats = json.load(file)
    ai_analiz(model, chats)




if __name__ == "__main__":
    asyncio.run(main())
