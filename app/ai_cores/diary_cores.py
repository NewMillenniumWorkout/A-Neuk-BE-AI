from typing import List
from app.models.diary_models import DiaryRequest, DiaryContent


def diary_generate(request: DiaryRequest) -> str:
    return f"{request} This is a diary_generate function"


def diary_split(request: str) -> List[str]:
    return ["This is a diary_split function"]


def diary_find_emotions(request: List[str]) -> List[DiaryContent]:
    content_list = []
    for idx, content in enumerate(request):
        content_list.append(
            DiaryContent(
                order_index=idx,
                original_content=content,
                recommend_emotion=["행복", "평온"],
            )
        )
    return content_list
