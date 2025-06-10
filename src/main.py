import os
from dotenv import load_dotenv
from telethon import TelegramClient
from get_date import get_date, client
import asyncio


async def main():
    
    await client.start() 
    await get_date(client)
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())  
