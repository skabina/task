import datetime
import os
from telethon import TelegramClient, events, sync
from dotenv import load_dotenv




 

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

client = TelegramClient('session_name', api_id, api_hash)


client = TelegramClient('session_name', api_id, api_hash)

one_month_ago = datetime.datetime.now() - datetime.timedelta(days=30)

