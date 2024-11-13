from typing import List

from app.models.diary_models import DiaryContent
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
import random
import dotenv

dotenv.load_dotenv()


class DiaryEmotionList(BaseModel):
    common_top1: str
    common_top2: str
    common_top3: str
    common_top4: str
    common_top5: str
    uncommon_top1: str
    uncommon_top2: str
    uncommon_top3: str
    uncommon_top4: str
    uncommon_top5: str


with open("emotions.txt", "r", encoding="utf-8") as f:
    emotions_db = [line.strip() for line in f.readlines()]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

output_parser = JsonOutputParser(pydantic_object=DiaryEmotionList)
format_instructions = output_parser.get_format_instructions()

# system_prompt = """
# 입력 문장은 사용자의 하루에 대해서 다룬 일기의 일부분입니다. 입력 문장에 대해서 다음의 작업을 수행해주세요.

# 1. 입력 문장의 상황에서 일기의 작성자가 느꼈을 법한 감정 총 10가지를 추출합니다.
# 2. common_top1~5는 일기 작성자가 느꼈을 것으로 추정되는 **보편적인** 감정 5개입니다.
# 3. uncommon_top1~5는 **보편적이지 않은, 비보편적인** 감정 5개입니다.
# 4. 예를 들어, '친구의 시상식에 참가했다"라는 문장에서 '행복'은 보편적인 감정이고, '질투', '부러움'은 비보편적인 감정입니다.
# 5. 모든 감정은 반드시 제공되는 421개의 감정 단어 목록 중에서 선택해야 합니다.
# """

system_prompt = """
The input sentence is part of a diary entry describing the user’s day. Please perform the following tasks to identify emotions the diary author may have felt but might not have fully noticed.

1. **Extract a total of 10 possible emotions** that the author may have felt in this context, taking into account any **emotional shifts or changes** within the sentence (e.g., if there’s an emotional transition, list the relevant emotions for each shift).
2. Classify the emotions into two categories:
   - **common_top1~5**: 5 **common emotions** likely felt in response to the diary’s context. These are emotions that are predictable or easily inferred from the situation.
   - **uncommon_top1~5**: 5 **uncommon emotions** (specific or unique feelings) that may have been felt. These emotions are less expected in the context but could represent inner thoughts or subtle nuances.
3. Ensure that **no emotions already present in the input sentence** are selected.
4. Consider any **overlapping emotions** within the same situation or event in the input (e.g., a mix of enjoyment with a hint of anxiety).
5. Select all emotions from the provided **list of 421 Korean emotional words**.
6. **Ensure the chosen emotions feel natural and contextually fitting** within the diary entry. Review each emotion to confirm its relevance.
"""

prompt = PromptTemplate(
    template="{prompt}\n{format_instructions}\nKorean emotional words:{emotion_list_with_comma}\nUser input:{query}\n",
    input_variables=["query", "emotion_list_with_comma"],
    partial_variables={
        "prompt": system_prompt,
        "format_instructions": format_instructions,
    },
)


async def find_emotions_from_sentence(sentence: str) -> List[str]:
    random.shuffle(emotions_db)
    chain = prompt | llm | output_parser
    result = await chain.ainvoke(
        {"query": sentence, "emotion_list_with_comma": ",".join(emotions_db)}
    )
    result_list = []
    for key, value in result.items():
        result_list.append(value)
    # print(f"sentence: {sentence}")
    # for key, value in result.items():
    #     print(f"{key}: {value}")
    # print("")
    return result_list


# if __name__ == "__main__":
#     request_example = [
#         "오늘은 종강하고 맞이한 첫 날이었다. 어제는 시험이 늦게 끝나서 피곤했지만, 집에 와서 오랜만에 운동도 하고 푹 쉬었다. 몸이 좀 개운해진 느낌이다. ",
#         "오늘은 늦잠을 자고 일어났다. 오랜만에 늦게까지 자서 그런지 몸이 한결 가벼웠다. ",
#         "오픈소스 프로젝트 수업에서 다른 팀들의 프로젝트를 데모해보는 시간이 있어서, 그걸 하느라 시간을 보냈다. ",
#         "다른 팀들 중에서 일기 작성 프로그램이 정말 마음에 들었다. 평소에 일기를 쓰고 싶었지만 혼자 쓰는 건 어렵고 자주 그만두곤 했다. 그런데 대화형으로 일기를 쓰는 방식이 부담도 적고 재미있을 것 같았다. ",
#         "그 후로는 비가 많이 와서 밖에 나가기가 망설여졌다. 원래는 피시방에 가서 게임을 하려 했는데, 아무래도 집에서 쉬는 게 나을 것 같았다. ",
#         "내일 부산 여행을 갈 예정이라 오늘은 집에서 여행 계획을 세우기로 했다. 맛집도 찾아보고 가고 싶은 곳 리스트도 정리하려고 한다. 내일이 기대된다. ",
#         "오늘 하루는 비교적 조용하게 보냈지만, 내일 여행을 생각하니 설렌다. 부산에서 좋은 추억 많이 만들고 오고 싶다. ",
#     ]
#     for content in request_example:
#         diary_find_emotions(content)


async def diary_find_emotions(request: List[str]) -> List[DiaryContent]:
    content_list = []
    for idx, content in enumerate(request):
        content_list.append(
            DiaryContent(
                order_index=idx,
                original_content=content,
                recommend_emotion= await find_emotions_from_sentence(content),
            )
        )
    return content_list
