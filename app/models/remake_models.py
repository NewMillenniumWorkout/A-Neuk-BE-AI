from pydantic import BaseModel


class RemakeRequest(BaseModel):
    original_content: str
    emotion_list: list[str]
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    original_content: "저녁에는 오랜만에 친구를 만나 파스타를 먹었다. 파스타가 정말 맛있었고, 친구와 근황을 이야기하며 웃음이 끊이질 않았다. 서로의 재밌는 이야기들 덕분에 시간 가는 줄 몰랐다. 친구와의 만남은 언제나 나에게 큰 에너지를 준다.",
                    emotion_list: [
                        "편안하다",
                        "행복하다",
                        "즐겁다",
                        "감회가 새롭다",
                        "신바람 나다",
                        "감동하다",
                    ],
                }
            ]
        }
    }


class RemakeResponse(BaseModel):
    remade_content: str
