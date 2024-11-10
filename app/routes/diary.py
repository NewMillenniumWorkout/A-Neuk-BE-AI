from fastapi import APIRouter
from app.models.diary_models import DiaryRequest, DiaryResponse
from app.ai_cores import diary_generate, diary_split, diary_find_emotions


router = APIRouter(prefix="/ai/diary", tags=["Diary"])


def debug_process(original, splitted, emotions):
    print("---Original---\n", original)
    print("\n")
    print("---Splitted---\n", splitted)
    print("\n")
    print("---Emotions---\n", emotions)
    print("\n")


@router.post("/", response_model=DiaryResponse)
def chat_post(request: DiaryRequest):
    original = diary_generate(request)
    splitted = diary_split(original)
    emotions = diary_find_emotions(splitted)
    debug_process(original, splitted, emotions)

    return DiaryResponse(chat_id=request.chat_id, content_list=emotions)
