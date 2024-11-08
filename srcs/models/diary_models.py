from pydantic import BaseModel
from typing import List
from srcs.models.chat_models import ChatRequest


class DiaryRequest(ChatRequest):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "chat_id": 0,
                    "messages": [
                        {
                            "role": "ASSITANT",
                            "message": "안녕 좋은 하루야! 오늘 하루는 어땠어?",
                        },
                        {"role": "MEMBER", "message": "반가워! 물론 좋았지"},
                        {"role": "ASSITANT", "message": "뭐가 재밌었어?"},
                        {"role": "MEMBER", "message": "맛있는 점심을 먹었어"},
                    ],
                }
            ]
        }
    }
