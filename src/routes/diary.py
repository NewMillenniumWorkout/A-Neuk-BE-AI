from fastapi import APIRouter, HTTPException
from src.models.diary_models import DiaryRequest, DiaryResponse, LLMError
from src.ai_cores import diary_generate, diary_split, diary_find_emotions
import time

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


async def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = await func(*args, **kwargs)
    elapsed_time = time.time() - start_time
    print(f"{func.__name__} executed in {elapsed_time:.2f} seconds.")
    return result


@router.post("/", response_model=DiaryResponse)
async def diary_post(request: DiaryRequest):
    try:
        original = await measure_time(diary_generate, request)
        splitted = await measure_time(diary_split, original)
        emotions = await measure_time(diary_find_emotions, splitted)

    except LLMError as e:
        raise HTTPException(status_code=500, detail=f"Diary generation failed: {e}")

    return DiaryResponse(chat_id=request.chat_id, content_list=emotions)
