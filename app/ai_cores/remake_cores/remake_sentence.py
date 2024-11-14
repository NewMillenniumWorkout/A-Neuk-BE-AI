from typing import List
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from app.models.remake_models import RemakeResponse

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

output_parser = JsonOutputParser(pydantic_object=RemakeResponse)
format_instructions = output_parser.get_format_instructions()

system_prompt = """
유저의 일기를 감정 리스트를 반영하여 다채롭고 자연스러운 문장으로 재구성해줘. 규칙은 다음과 같아.

1. original_sentence는 유저가 하루 중 느낀 감정이 담긴 일기 내용이야. 예시:
   - 예시 original_sentence: 저녁에는 오랜만에 친구를 만나 파스타를 먹었다. 파스타가 정말 맛있었고, 친구와 근황을 이야기하며 웃음이 끊이질 않았다. 서로의 재밌는 이야기들 덕분에 시간 가는 줄 몰랐다. 친구와의 만남은 언제나 나에게 큰 에너지를 준다.
   
2. emotion_list는 해당 순간 유저가 느낀 감정 목록이야. 이 감정들을 최대한 자연스럽게 녹여서 문장을 재구성해야 해.
   - 예시 emotion_list: 편안하다,행복하다,즐겁다,신바람 나다

3. 새롭게 재구성한 문장을 remade_content에 담아줘. 유저가 느꼈을 감정과 상황이 자연스럽게 드러나도록 주의해줘.
   - 예시 remade_content: 오랜만에 만난 친구와 함께한 저녁은 편안하고 행복한 시간이었다. 맛있는 파스타를 나누며 서로의 근황을 전하다 보니 웃음이 끊이질 않았고, 즐겁고 신바람 나는 대화 속에 시간 가는 줄 몰랐다. 친구와의 만남이 나에게 얼마나 소중한 에너지가 되는지 다시금 느꼈다.
"""

prompt = PromptTemplate(
    template="{prompt}\n{format_instructions}\nOriginal sentence:{query}\nTarget Korean emotional words:{emotion_list_with_comma}\n",
    input_variables=["query", "emotion_list_with_comma"],
    partial_variables={
        "prompt": system_prompt,
        "format_instructions": format_instructions,
    },
)


async def remake_sentence(origin: str, emotions: List[str]) -> str:
    chain = prompt | llm | output_parser
    result = await chain.ainvoke(
        {"query": origin, "emotion_list_with_comma": ",".join(emotions)}
    )
    # print(result["remade_content"])
    return result["remade_content"]
