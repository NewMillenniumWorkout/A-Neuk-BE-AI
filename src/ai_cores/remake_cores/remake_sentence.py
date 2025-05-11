from typing import List
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from src.models.remake_models import RemakeResponse
from langchain_google_genai import ChatGoogleGenerativeAI

# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.25)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-04-17")

output_parser = JsonOutputParser(pydantic_object=RemakeResponse)
format_instructions = output_parser.get_format_instructions()

system_prompt = """
유저의 일기를 감정 리스트를 반영하여 **다채롭고 자연스러운 문장으로 재구성**하는 과제입니다. 답변은 한국어로 작성해주세요.

### 과제 수행 규칙
1. 감정이 모호한 경우, 문맥을 고려해 가장 자연스럽게 표현되는 방향으로 재구성합니다.
2. original_sentence와 emotion_list에서 나타난 유저의 감정을 존중하며, 긍정적이든 부정적이든 감정의 본질을 그대로 반영합니다.
3. original_sentence는 유저가 하루 중 느낀 감정이 담긴 일기 내용입니다.
   - 예시 original_sentence: 저녁에는 오랜만에 친구를 만나 파스타를 먹었다. 파스타가 정말 맛있었고, 친구와 근황을 이야기하며 웃음이 끊이질 않았다. 서로의 재밌는 이야기들 덕분에 시간 가는 줄 몰랐다. 친구와의 만남은 언제나 나에게 큰 에너지를 준다.
4. emotion_list는 해당 순간 유저가 느낀 감정 목록입니다. 이 감정들을 최대한 자연스럽게 녹여서 문장을 재구성합니다.
   - 예시 emotion_list: 편안하다,행복하다,즐겁다,신바람 나다
5. 새롭게 재구성한 문장을 remade_content에 출력합니다. 유저가 느낀 감정과 상황이 자연스럽게 드러나도록 주의하여 재구성합니다.
   - 예시 remade_content: 오랜만에 만난 친구와 함께한 저녁은 편안하고 행복한 시간이었다. 맛있는 파스타를 나누며 서로의 근황을 전하다 보니 웃음이 끊이질 않았고, 즐겁고 신바람 나는 대화 속에 시간 가는 줄 몰랐다. 친구와의 만남이 나에게 얼마나 소중한 에너지가 되는지 다시금 느꼈다.
6. 재구성한 문장은 한국어로 작성합니다. original_sentence의 말투와 유사하게 작성하는 것이 좋습니다.
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
    remade_content = result["remade_content"]
    print(f"origin:{origin}, emotions:{emotions}, remade:{remade_content}")
    return remade_content
