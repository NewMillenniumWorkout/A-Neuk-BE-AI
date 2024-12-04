import random
from typing import List
from src.models.diary_models import DiaryContent, DiaryEmotionList, DirayCategoryList
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
import asyncio
import copy

emotion_categories = [
    "공포",
    "기쁨",
    "기타",
    "놀람",
    "분노",
    "슬픔",
    "중성",
    "지루",
    "통증",
    "혐오",
    "흥미",
]
emotion_dict = {category: [] for category in emotion_categories}

file_path = "emotions.txt"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            key, value = line.strip().split("\t")
            if key in emotion_dict:
                emotion_dict[key].append(value)
except FileNotFoundError:
    print(f"파일 '{file_path}'이(가) 존재하지 않습니다.")
except Exception as e:
    print(f"오류 발생: {e}")

# # 결과 출력
# for key, values in emotion_dict.items():
#     print(f"{key}: {values}")

llms = [
    ChatOpenAI(model="gpt-4o-mini", temperature=0),
    ChatOpenAI(model="gpt-4o-mini", temperature=0.25),
    ChatOpenAI(model="gpt-4o-mini", temperature=0.5),
    ChatOpenAI(model="gpt-4o-mini", temperature=0.75),
]

find_category_output_parser = JsonOutputParser(pydantic_object=DirayCategoryList)
find_category_format_instructions = (
    find_category_output_parser.get_format_instructions()
)
find_category_system_prompt = (
    """
다음은 주어진 문장에서 드러날 수 있는 감정을 분석하는 과제입니다. 주어진 11개의 감정 중에서 문맥에 적합하고 자연스러운 감정을 도출해야 합니다.

### 감정 목록:
다음은 주어진 감정 목록과 그 id입니다. 형식: {{감정 id}}.{{감정 이름}}, {{감정 id}}.{{감정 이름}}, ...:
"""
    + ", ".join([f"{i}.{emotion}" for i, emotion in enumerate(emotion_categories)])
    + """

### 작업 요구 사항:
1. **총 3개의 감정 id**를 추출합니다. 문맥에서의 **감정 변화**(emotional shifts)도 고려하여, 해당 문장에서 느껴졌을 가능성이 있는 감정의 id를 출력합니다.
2. 높은 우선 순위로 3개의 감정 id를 선택합니다.
   - **category1**: 이는 문맥에 **가장 지배적이고 쉽게 유추할 수 있는 가장 가능성이 높은** 감정입니다.
   - **category2**: 이는 **category1 다음으로 가능성이 높은** 감정입니다.
   - **category3**: 상황에서 **특수하고, 덜 예상되지만 가능성 있는** 감정입니다. 문맥상 미묘하거나 독특하게 느껴질 수 있는 감정입니다.
3. 동일한 상황에서 **겹치는 감정**(e.g., 즐거움과 동시에 느껴지는 불안함)도 고려합니다.
5. 최종적으로, **문맥과 자연스럽게 연결되는 감정**인지 검토 후 확정합니다.
"""
)
find_category_prompt = PromptTemplate(
    template="{prompt}\n{find_category_format_instructions}\n\nUser input:{query}",
    input_variables=["query"],
    partial_variables={
        "prompt": find_category_system_prompt,
        "find_category_format_instructions": find_category_format_instructions,
    },
)


find_emotions_output_parser = JsonOutputParser(pydantic_object=DiaryEmotionList)
find_emotions_format_instructions = (
    find_emotions_output_parser.get_format_instructions()
)
find_emotions_system_prompt1 = """
다음은 주어진 문장에서 드러날 수 있는 감정을 분석하는 과제입니다. 감정은 **제시된 한국어 감정 단어 중에서 선택**하며, 문맥에 적합하고 자연스러운 감정을 도출해야 합니다.

### 감정 목록:
다음은 주어진 감정 목록과 그 id입니다. 형식: {{감정 id}}.{{감정 이름}}, {{감정 id}}.{{감정 이름}}, ...:
"""
find_emotions_system_prompt2 = """
### 작업 요구 사항:
1. **총 10개의 감정 id**를 추출합니다. 문맥에서의 **감정 변화**(emotional shifts)도 고려하여, 해당 문장에서 느껴졌을 가능성이 있는 감정 id를 선택합니다.
2. 추출한 감정을 아래 두 가지 범주로 분류합니다:
   - **common_top1~7**: 상황에서 **예상 가능한 감정 id** 7가지. 이는 문맥에 쉽게 유추할 수 있는 일반적인 감정입니다.
   - **uncommon_top1~3**: 상황에서 **덜 예상되지만 가능성 있는 감정 id** 3가지. 문맥상 미묘하거나 독특하게 느껴질 수 있는 감정입니다.
3. **문장 내에 이미 드러나 있는 감정 표현은 제외**합니다.
4. 동일한 상황에서 **겹치는 감정**(e.g., 즐거움과 동시에 느껴지는 불안함)도 고려합니다.
5. 최종적으로, **문맥과 자연스럽게 연결되는 감정**인지 검토 후 확정합니다.
"""
find_emotions_prompt = PromptTemplate(
    template="{prompt1}\n{emotion_list_with_comma}\n{prompt2}\n{find_emotions_format_instructions}\nUser input:{query}\n",
    input_variables=["query", "emotion_list_with_comma"],
    partial_variables={
        "prompt1": find_emotions_system_prompt1,
        "prompt2": find_emotions_system_prompt2,
        "find_emotions_format_instructions": find_emotions_format_instructions,
    },
)


async def find_emotions_from_sentence(sentence: str, category_id: int) -> List[str]:
    result_list = []
    emotions_db_copy = copy.deepcopy(emotion_dict[emotion_categories[category_id]])
    random.shuffle(emotions_db_copy)
    emotions_chain = find_emotions_prompt | llms[0] | find_emotions_output_parser
    result = await emotions_chain.ainvoke(
        {
            "query": sentence,
            "emotion_list_with_comma": ", ".join(
                [f"{i}.{emotion}" for i, emotion in enumerate(emotions_db_copy)]
            ),
        }
    )
    for key, emotion_id in result.items():
        if key.startswith("common") or key.startswith("uncommon"):
            if emotion_id < 0 or emotion_id >= len(emotions_db_copy):
                pass
            result_list.append(emotions_db_copy[emotion_id])
    return result_list


async def find_category_from_sentence(sentence: str) -> List[str]:
    category_chain = find_category_prompt | llms[0] | find_category_output_parser
    result = await category_chain.ainvoke({"query": sentence})

    tasks = []
    for category_id in result.values():
        if category_id < 0 or category_id >= len(emotion_categories):
            category_id = 2
        tasks.append(find_emotions_from_sentence(sentence, category_id))

    results = await asyncio.gather(*tasks)

    result_list = []
    for sublist in results:
        result_list.extend(sublist)

    unique_list = []
    [unique_list.append(x) for x in result_list if x not in unique_list]
    return unique_list


async def diary_find_emotions(request: List[str]) -> List[DiaryContent]:
    tasks = [find_category_from_sentence(content) for content in request]
    results = await asyncio.gather(*tasks)

    content_list = [
        DiaryContent(
            order_index=idx, original_content=content, recommend_emotion=result
        )
        for idx, (content, result) in enumerate(zip(request, results))
    ]

    return content_list
