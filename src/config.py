import os

from dotenv import load_dotenv

load_dotenv()

ai_api_key = os.getenv('AI_API_KEY')
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')