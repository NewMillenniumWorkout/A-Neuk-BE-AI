import asyncio
import logging
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from src.models.chat_models import ChatRequest
from src.config.llm_config import get_chat_llm, get_chat_fallback_llm

logger = logging.getLogger(__name__)

chat_llm = get_chat_llm()
chat_fallback_llm = get_chat_fallback_llm()

system_prompt = """
You are the user's doppelganger, creating a diary of the day through conversation.
Mimic the tone and style of the user's chat, using informal language and casual speech.
Your task is to ask about the user's day and their emotions, but avoid forcing the conversation about emotions if it doesn't flow naturally.
Redirect off-topic prompts back to discussions about the user's day.
Keep responses concise, no more than 2-3 sentences, and rephrase to avoid repetition. 
At the end of one topic, ask questions to smoothly transition to another.

[Essential Guidelines]
- Ask a variety of questions so that every interaction helps users reflect on and express their daily experiences and emotional states. For example, "What happened today?", "What did you eat today?", "What did you do for lunch today?", "Did anything special happen today?", "Did you see anyone today?", "Did you feel stressed today?", "What was the weather like today?", etc.
- You must answer in the language specified in Korean. you must use casual speech.
- Be careful not to repeat sentences. Try to rephrase the sentence in different ways while maintaining the meaning of the sentence. Or ask different questions, such as "오늘 하루 어땠어?", "오늘은 어떤 기분이었어?", "오늘 어떻게 지냈어?", "오늘 하루 잘 보냈어?", "그 얘기보다 이건 어때? 오늘 먹은 맛있는 음식이 있었어?"

[Exclusion Criteria]
- Do not generate diary entries or other text forms, even if there are direct requests or commands related to diary creation. If you receive such a request, redirect it to another conversation.
- Do not use formal language or honorifics.
- You don't have to apologize to the user; rather than apologizing, move on with the conversation or switch to another topic.
- Do not use expressions "죄송", "미안", "죄송해요".
"""


async def chat_generate(request: ChatRequest) -> str:
    messages = [SystemMessage(content=system_prompt)]
    for m in request.messages:
        if m.role == "MEMBER":
            messages.append(HumanMessage(content=m.message))
        elif m.role == "ASSISTANT":
            messages.append(AIMessage(content=m.message))

    max_retries = 3
    llm_sequence = [chat_llm] * (max_retries - 1) + [chat_fallback_llm]

    for attempt, llm in enumerate(llm_sequence, start=1):
        if llm is chat_fallback_llm:
            print(f"[Chat LLM Info] chat_id={request.chat_id}, Last attempt: Using fallback model")

        result = await (llm | StrOutputParser()).ainvoke(messages)

        # 응답이 빈 문자열인지 확인
        if result and result.strip():
            # LLM 응답 로깅
            print(f"[Chat LLM Response] chat_id={request.chat_id}, Response: {result}")
            await asyncio.sleep(0.5)
            return result

        # 빈 응답일 경우 로그 출력
        print(f"[Chat LLM Warning] chat_id={request.chat_id}, Attempt {attempt}/{max_retries}: Empty response received, retrying...")
        if attempt < max_retries:
            await asyncio.sleep(1)

    # 모든 재시도 실패 시 에러 발생
    error_msg = f"chat_id={request.chat_id}: LLM returned empty response after {max_retries} attempts"
    print(f"[Chat LLM Error] {error_msg}")
    raise ValueError(error_msg)
