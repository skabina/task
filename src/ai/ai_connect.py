import os
import google.generativeai as genai
from config.settings import settings  

def ai_connect():
    genai.configure(api_key=settings.env.AI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    print("[DEBUG] os.environ['AI_API_KEY'] =", os.environ.get("AI_API_KEY"))

    return model

ai_connect()  # Initialize the AI connection when this module is imported