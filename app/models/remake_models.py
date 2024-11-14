from pydantic import BaseModel


class RemakeRequest(BaseModel):
    original_content: str
    emotion_list: list[str]
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "original_content": "집에 돌아와서는 차 한 잔과 함께 책을 읽었다. 하루의 마무리로 이보다 더 좋을 수 있을까 싶을 정도로 평화로웠다. 오늘 하루의 소소한 행복들을 마음에 담으며, 감사한 마음으로 잠자리에 든다.",
                    "emotion_list": [
                        "행복하다",
                        "감사하다",
                        "만족하다",
                        "편안하다",
                    ],
                }
            ]
        }
    }


class RemakeResponse(BaseModel):
    remade_content: str
