from typing import List
from app.models.diary_models import DiaryRequest, DiaryContent


def diary_generate(request: DiaryRequest) -> str:
    return f"{request} This is a diary_generate function"
