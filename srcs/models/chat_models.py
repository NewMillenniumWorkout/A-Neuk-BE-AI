from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str
    message: str


class ChatRequest(BaseModel):
    chat_id: int
    messages: list[ChatMessage]


class ChatResponse(BaseModel):
    role: str
    message: str
