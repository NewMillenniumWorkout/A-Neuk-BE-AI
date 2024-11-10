from fastapi import APIRouter
from app.models.chat_models import ChatRequest, ChatResponse
from app.ai_cores.chat_cores import chat_generate


router = APIRouter(prefix="/ai/chat", tags=["Chat"])


@router.post("/", response_model=ChatResponse)
def chat_post(request: ChatRequest):
    return ChatResponse(
        chat_id=request.chat_id,
        role="ASSISTANT",
        message= chat_generate(request)
    )
