import os
import asyncio

from telethon import TelegramClient
from get_date import TelegramAccount
from ai_analiz import analiz_ai

async def main():
    
    # get_date працює і зчитує 10 останніх діалогів за останній місяць
    # Але окільки в мене було діалогів я зробив 10 діалогів вручну які відповідають запису 
    
    account = TelegramAccount()
    await account.start()
    await account.get_date()
    await account.disconnect()
  
    #analiz_ai() 

if __name__ == "__main__":
    asyncio.run(main())  
