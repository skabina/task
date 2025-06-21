import json
import asyncio
from telegram_client.client import get_client
from telegram_client.fetch_date import fetch_date
from ai.ai_connect import ai_connect
from ai.ai_analiz import ai_analiz

from telegram_client.crud import correct_message, save_json

async def main():
    
    client = get_client()
    await client.start()
    chat_list = await fetch_date(client)

    chat_output = correct_message(chat_list)
    save_json(chat_output)

    model = ai_connect()
    ai_analiz(model, chat_output)
    

if __name__ == "__main__":
    asyncio.run(main())
