from typing import List
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import dotenv
import os
from langchain_core.output_parsers import StrOutputParser


llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
output_parser = StrOutputParser()

system_prompt = """
20개의 단어는 모두 감정을 나타내는 한국어 단어야.
탭으로 감정단어, 대분류, 뜻이 제시되어있어.
너의 역할은 20개의 감정 단어에 대해서 적절한 예문을 생성하고 출력하는 거야. 예문은 한 줄에 하나씩 출력하면 돼.

단어와 예문 사이는 쉼표 ','로 구분해줘.
예시는 다음과 같아. 1인칭 시점에서 서술된 예문을 선호해.

**예시**
경이롭다,갓 태어난 아기의 작은 손과 발을 보니 생명의 신비로움에 경이로움을 느꼈다.
민망하다,어른들 앞에서 아이처럼 떼를 쓰는 동생을 보니 민망했다.


**유저 입력**
"""


prompt = PromptTemplate(
    template="{system_prompt}\nUser input:{query}",
    input_variables=["query"],
    partial_variables={"system_prompt": system_prompt},
)


def get_example(origin) -> str:
    chain = prompt | llm | output_parser
    result = chain.invoke({"query": origin})
    return result


def process_emotions(file_path: str, output_file: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        emotions = [line.strip() for line in lines if line.strip()]

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("")

        # 20개씩 묶어서 처리
        chunk_size = 20
        for i in range(0, len(emotions), chunk_size):
            chunk = emotions[i : i + chunk_size]
            print(f"Processing chunk {i // chunk_size + 1}...")
            result = get_example(chunk)

            with open(output_file, "a", encoding="utf-8") as f:
                f.write(f"Chunk {i // chunk_size + 1}:\n")
                f.write(result + "\n\n")

    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    dotenv.load_dotenv("../../../.env")
    file_path = "emotions.txt"
    output_file = "output.txt"
    process_emotions(file_path, output_file)
