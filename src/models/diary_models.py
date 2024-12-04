from pydantic import BaseModel
from typing import List
from src.models.chat_models import ChatRequest


class DiaryRequest(ChatRequest):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "chat_id": 0,
                    "messages": [
                        {
                            "role": "ASSISTANT",
                            "message": "안녕! 오늘 하루는 어땠어? 특별한 일이 있었어?",
                        },
                        {
                            "role": "MEMBER",
                            "message": "오늘 날씨가 좋아서 산책을 했어.",
                        },
                        {
                            "role": "ASSISTANT",
                            "message": "와, 산책이라니! 어디로 갔어? 경치가 어땠어?",
                        },
                        {
                            "role": "MEMBER",
                            "message": "공원에 갔는데, 나무들이 색색으로 변해서 너무 예뻤어.",
                        },
                        {
                            "role": "ASSISTANT",
                            "message": "멋지네! 산책하면서 또 특별히 느낀 점이 있었어?",
                        },
                        {
                            "role": "MEMBER",
                            "message": "자연 속에서 시간을 보내니 기분이 상쾌해졌어. 스트레스가 확 풀렸어.",
                        },
                        {
                            "role": "ASSISTANT",
                            "message": "그랬구나! 산책 외에 또 즐거운 일이 있었을까?",
                        },
                        {
                            "role": "MEMBER",
                            "message": "친구랑 저녁에 만나서 맛있는 파스타도 먹었어.",
                        },
                        {
                            "role": "ASSISTANT",
                            "message": "좋아 보이네! 파스타는 어땠어? 친구랑 무슨 이야기 했어?",
                        },
                        {
                            "role": "MEMBER",
                            "message": "정말 맛있었고, 친구랑 오랜만에 근황 얘기 많이 했어. 서로 재밌는 일들이 많더라고.",
                        },
                        {
                            "role": "ASSISTANT",
                            "message": "들으니 나까지 기분이 좋아지네! 오늘 하루 마무리는 어땠어?",
                        },
                        {
                            "role": "MEMBER",
                            "message": "집에 와서 차 한 잔 마시며 책을 읽었어. 정말 평화로운 하루였어.",
                        },
                        {
                            "role": "ASSISTANT",
                            "message": "완벽한 하루였네! 오늘 느낀 감정들을 일기에 담아보면 좋을 것 같아.",
                        },
                    ],
                }
            ]
        }
    }


class DiaryContent(BaseModel):
    order_index: int
    original_content: str
    recommend_emotion: List[str]


class DiaryResponse(BaseModel):
    chat_id: int
    content_list: List[DiaryContent]


class DairyStrList(BaseModel):
    content_list: List[str]


class LLMError(Exception):
    pass


class DiaryEmotionList(BaseModel):
    common_top1: int
    common_top2: int
    common_top3: int
    common_top4: int
    common_top5: int
    common_top6: int
    common_top7: int
    uncommon_top1: int
    uncommon_top2: int
    uncommon_top3: int


class DirayCategoryList(BaseModel):
    category1: int
    category2: int
    category3: int
