from fastapi import APIRouter
from srcs.models.chat_models import ChatRequest, ChatResponse


router = APIRouter(prefix="/ai/chat", tags=["Chat"])


@router.post("/", response_model=ChatResponse)
def ai_chat(request: ChatRequest):
    return ChatResponse(
        role="ASSISTANT",
        message=f"TEST: {request.chat_id}, {request.messages[0].message}",
    )
