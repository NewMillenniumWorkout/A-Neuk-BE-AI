from fastapi import APIRouter
from app.models.diary_models import DiaryRequest, DiaryResponse
from app.ai_cores import diary_generate, diary_split, diary_find_emotions


router = APIRouter(prefix="/ai/diary", tags=["Diary"])


@router.post("/", response_model=DiaryResponse)
def chat_post(request: DiaryRequest):
    diary_original = diary_generate(request)
    diary_splitted = diary_split(diary_original)
    diary_emotions = diary_find_emotions(diary_splitted)

    return DiaryResponse(chat_id=request.chat_id, content_list=diary_emotions)
