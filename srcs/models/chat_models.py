from pydantic import BaseModel
from typing import List


class ChatMessage(BaseModel):
    role: str
    message: str


class ChatRequest(BaseModel):
    chat_id: int
    messages: List[ChatMessage]


class ChatResponse(BaseModel):
    role: str
    message: str
