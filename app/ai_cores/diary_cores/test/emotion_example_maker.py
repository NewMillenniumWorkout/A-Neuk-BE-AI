from langchain_core.output_parsers import StrOutputParser
from langchain.schema.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate
import dotenv

dotenv.load_dotenv()


class ExampleModel(BaseModel):
    input: str
    output: str


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

output_parser = JsonOutputParser(pydantic_object=ExampleModel)
format_instructions = output_parser.get_format_instructions()


system_prompt = """
한국어 감정 단어에 맞는 예문을 작성합니다. 각 단어에 적절하게 연결된 상황과 어울리는 문장을 제공합니다. 문장들은 현실적이고 감정을 잘 표현할 수 있는 예문으로 만듭니다. 가능한 한 단어가 포함된 자연스러운 문장으로 표현합니다.

인풋 단어 예시:
겁나다
공포감
급박하다 ...

예문 형식 예시:
겁나다 - 그곳에 들어서는 순간 이상한 기운이 감돌아 괜히 겁이 났다.
공포감 - 어두운 골목길에서 발소리가 들려오자 가슴 속에 공포감이 밀려왔다.
급박하다 - 사건이 발생한 이후 상황은 급박하게 돌아가기 시작했다. ...

단어마다 한 문장씩 제공하세요.
"""


prompt = PromptTemplate(
    template="{system_prompt}\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={
        "system_prompt": system_prompt,
        "format_instructions": format_instructions,
    },
)


def make_example(query: str) -> str:
    chain = prompt | llm | output_parser
    result = chain.invoke({"query": query})
    return result["output"]


if __name__ == "__main__":
    # emotions.txt 파일에서 감정 단어를 읽어오기
    with open("emotions.txt", "r", encoding="utf-8") as f:
        emotions = [line.strip() for line in f.readlines()]

    # emotions_with_examples.txt 파일에 작성
    with open("emotions_with_examples.txt", "w", encoding="utf-8") as f:
        for emotion in emotions:
            example = make_example(emotion)
            f.write(f"{emotion} - {example}\n")
            print(f"{emotion} - {example}")
