from typing import List
from app.models.diary_models import DiaryContent


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
