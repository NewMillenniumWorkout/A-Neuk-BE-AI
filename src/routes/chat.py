from fastapi import APIRouter
from src.models.chat_models import ChatRequest, ChatResponse
from src.ai_cores import chat_generate


router = APIRouter(prefix="/ai/chat", tags=["Chat"])


@router.post("/", response_model=ChatResponse)
async def chat_post(request: ChatRequest):
    result = await chat_generate(request)
    return ChatResponse(chat_id=request.chat_id, role="ASSISTANT", message=result)
