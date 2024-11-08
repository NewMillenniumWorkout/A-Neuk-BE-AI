from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "이 시스템은 천문학 질문에 답변할 수 있습니다."),
        ("user", "{user_input}"),
    ]
)

chat_llm = ChatOpenAI(model="gpt-4o-mini")

chain = chat_prompt | chat_llm | StrOutputParser()

print(chain.invoke({"user_input" : "천문학에서 태양계의 몇 번째 행성인지 알려줘"}))
