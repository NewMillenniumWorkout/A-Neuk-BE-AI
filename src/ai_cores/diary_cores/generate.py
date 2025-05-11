from langchain_core.output_parsers import StrOutputParser
from langchain.schema.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from src.models.diary_models import DiaryRequest, LLMError
from langchain_google_genai import ChatGoogleGenerativeAI


# chat_llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
chat_llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-04-17")

default_diary_1 = """
수현, 명석과의 먹방의 날 ,, 수현언니 시험 끝난 기념으로 상도에 새로 생긴 돼지한약방..?에 갔다. 가격은 좀 있었지만 고기 다 구워주시고 맛도 있었다!!
돼지고기를 저렇게 자개에 가져오는게 넘 웃겼다 ,, 고급진데.. 웃겨,, ㅋㅋㅋㅋㅋ 1차는 간단하게 고기만 먹고 2차로 브롱스 가서 피자랑 윙봉에 맥주 마셨다!
브롱스 가보고싶다가 처음 가봤는데 맥주 종류 엄청 많고 피자도 맛있었다! 저 맥주 뭐였는지 기억은 안나지만 특이해서 한번쯤 먹어볼만 했다.
생크림이랑 아이스크림 들어있어서 그나마 먹었지 맥주 자체는 쫌 썼다.. 이날 진짜 너무 많이 먹었다...
"""
default_diary_2 = f"""
미용실 가서 머리 하고 유진이를 만났다 ! 세심정 갔다가 카페 갔는데 쉬지 않고 말했다.
만나면 이야기밖에 안하지만 너무 재밌어 ,, 할 얘기 너무 많아~~~ 왜 항상 그런 일이 있고 직후에 너를 만나게 되는지는 모르겠지만 ...
저번과 다름없이 또 너를 만났고.. 또 울었다 .. 다음에는 안 울고 재밌는 일만 가득 가지고 만나야지 ..,, 유진아 보고 있니 ~~~ 보고싶다 ~~~~
"""
default_diary_3 = """
드디어 !!! 혜윤이를 만났다. 매머드 그만 두고 처음 봤다. 복학해서 시험기간인 혜윤이었지만 ,,, 날 만나줬다...
9시 쯤 만나서 아마도가서 가볍게 맥주 한 잔 했다. 혜윤이 여행 이야기부터~ 이런저런 이야기들 많이 듣고 내 이야기도 많이 해줬다.
시간가는줄 모르고 이야기했다. 맥주 한잔에 얼굴 빨개진 혜윤이 너무 귀여웠다. 매머드 인연들 넘 소즁해
"""

system_prompt = f"""
Craft a diary entry that meticulously captures the essence of our preceding dialogue.
Remember to create a diary for "user", not "assistant".
[Essential Guidelines]
```
1. Diary Entry Creation: Mimic commonly used terms and expressions in user conversations.
2. Content clarity: You should only produce the diary itself. You should not produce any additional information, such as "[Today's Diary]" or "Your diary is complete".
3. Language Compliance: It is imperative that the entry adheres to the language specifications outlined in [Languages]. Failure to comply with this requirement could result in disqualification.
4. Write in a descriptive narrative interspersed with soliloquy, focusing on personal insights and avoiding any conversational tone.
```
[Exclusion Criteria]
```
It's crucial to note that the diary should exclusively document conversations regarding the events of the day and the emotions associated with those events.
Any dialogue not pertaining to today's occurrences or emotions should be meticulously omitted from the diary content.
This ensures the diary remains focused and relevant to the day's experiences and feelings, honoring the integrity of a true daily record.
It shouldn't be written as if the user is speaking to someone else. Keep in mind that it's a diary.
Your purpose is to write a diary for “user”. The dialog with “assistant” is to elicit the contents of user's diary. The assistant's lines should not go into the diary.
You should never write a diary based on the contents of an example of a generated diary. This is just an example of a diary.
```
[Example of Gerenated Diary]
```
Example1: {default_diary_1}
```
```
Example2: {default_diary_2}
```
```
Example3: {default_diary_3}
```
[Languages]
- Korean : informal language
- example : "했다" instead of "했어" / "없었어" instead of "없었어요" / "좋았다" instead of "좋았어"
"""


async def diary_generate(request: DiaryRequest) -> str:
    messages = [SystemMessage(content=system_prompt)]
    for m in request.messages:
        if m.role == "MEMBER":
            messages.append(HumanMessage(content=m.message))
        elif m.role == "ASSISTANT":
            messages.append(AIMessage(content=m.message))
    messages.append(
        HumanMessage(content="이제 우리가 나눈 대화 내용을 기반으로 일기를 생성해줘.")
    )

    chain = chat_llm | StrOutputParser()
    try:
        result = await chain.ainvoke(messages)
        return result
    except Exception as e:
        raise LLMError("Failed to generate a diary entry.")
