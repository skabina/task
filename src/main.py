import os
from dotenv import load_dotenv
from telethon import TelegramClient
from getDate import get_Date, client
import asyncio


async def main():
    
    await client.start() 
    await get_Date(client)
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())  
