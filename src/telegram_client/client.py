from telethon import TelegramClient
from telethon.errors import FloodWaitError
from config.settings import settings  



def get_client():
   client = TelegramClient('date', settings.env.API_ID, settings.env.API_HASH)
   return client
    


