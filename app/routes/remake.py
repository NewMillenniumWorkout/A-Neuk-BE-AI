from fastapi import APIRouter, HTTPException
from app.models.remake_models import RemakeRequest, RemakeResponse
from ai_cores import remake_sentence


router = APIRouter(prefix="/ai/remake", tags=["Remake"])


@router.post("/", response_model=RemakeResponse)
async def diary_post(request: RemakeRequest):
    remade_content = await remake_sentence(request)
    return RemakeResponse(remade_content=remade_content)
