from typing import List
from pydantic import BaseModel

class ChatMessage(BaseModel):
    sender: str
    time: str
    content: str

class ChatInfo(BaseModel):
    chat_id: int
    chat_name: str
    messages: List[ChatMessage] 
    