from fastapi import APIRouter
from srcs.models.chat_models import ChatRequest, ChatResponse
from srcs.ai_cores.chat_cores import chat_generate


router = APIRouter(prefix="/ai/chat", tags=["Chat"])


@router.post("/", response_model=ChatResponse)
def chat_post(request: ChatRequest):
    return ChatResponse(
        role="ASSISTANT",
        message= chat_generate(request)
    )
