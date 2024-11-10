from fastapi import APIRouter, HTTPException
from app.models.diary_models import DiaryRequest, DiaryResponse, LLMError
from app.ai_cores import diary_generate, diary_split, diary_find_emotions


router = APIRouter(prefix="/ai/diary", tags=["Diary"])


def debug_process(original, splitted, emotions):
    print("---Original---\n", original)
    print("\n")
    print("---Splitted---")
    for idx, content in enumerate(splitted):
        print(f"{idx}. {content}")
    print("\n")
    print("---Emotions---")
    for idx, content in enumerate(emotions):
        print(f"{idx}. {content.recommend_emotion}")
    print("\n")


@router.post("/", response_model=DiaryResponse)
def diary_post(request: DiaryRequest):
    try:
        original = diary_generate(request)
        splitted = diary_split(original)
        emotions = diary_find_emotions(splitted)
        debug_process(original, splitted, emotions)
    except LLMError as e:
        raise HTTPException(status_code=500, detail=f"Diary generation failed: {e}")

    return DiaryResponse(chat_id=request.chat_id, content_list=emotions)
