import os
import random
import faiss
import numpy as np
from typing import List
from src.models.diary_models import DiaryContent, DiaryEmotionList
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.embeddings import OpenAIEmbeddings
import asyncio
import copy

with open("emotions.txt", "r", encoding="utf-8") as f:
    emotions_db = [line.strip() for line in f.readlines()]

llms = [
    ChatOpenAI(model="gpt-4o-mini", temperature=0),
    ChatOpenAI(model="gpt-4o-mini", temperature=0.25),
    ChatOpenAI(model="gpt-4o-mini", temperature=0.5),
    ChatOpenAI(model="gpt-4o-mini", temperature=0.75),
]
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")

output_parser = JsonOutputParser(pydantic_object=DiaryEmotionList)
format_instructions = output_parser.get_format_instructions()

system_prompt = """
다음은 주어진 문장에서 드러날 수 있는 감정을 분석하는 과제입니다. 감정은 한국어 감정 단어 414개 중에서 선택하며, 문맥에 적합하고 자연스러운 감정을 도출해야 합니다.

### 작업 요구 사항:

1. **총 10개의 가능한 감정**을 추출합니다. 문맥에서의 **감정 변화**(emotional shifts)도 고려하여, 해당 문장에서 느껴졌을 가능성이 있는 감정을 도출합니다.
2. 추출한 감정을 아래 두 가지 범주로 분류합니다:
   - **common_top1~7**: 상황에서 **예상 가능한 감정** 7가지. 이는 문맥에 쉽게 유추할 수 있는 일반적인 감정입니다.
   - **uncommon_top1~3**: 상황에서 **덜 예상되지만 가능성 있는 감정** 3가지. 문맥상 미묘하거나 독특하게 느껴질 수 있는 감정입니다.
3. **문장 내에 이미 드러나 있는 감정 표현은 제외**합니다.
4. 동일한 상황에서 **겹치는 감정**(e.g., 즐거움과 동시에 느껴지는 불안함)도 고려합니다.
5. 최종적으로, **문맥과 자연스럽게 연결되는 감정**인지 검토 후 확정합니다.
"""

prompt = PromptTemplate(
    template="{prompt}\n{format_instructions}\nKorean emotional words:{emotion_list_with_comma}\nUser input:{query}\n",
    input_variables=["query", "emotion_list_with_comma"],
    partial_variables={
        "prompt": system_prompt,
        "format_instructions": format_instructions,
    },
)

# FAISS 인덱스 및 레이블 파일이 이미 존재하는지 확인
if os.path.exists("emotion_embeddings.index") and os.path.exists("emotion_labels.npy"):
    faiss_index = faiss.read_index("emotion_embeddings.index")
    emotion_labels = np.load("emotion_labels.npy", allow_pickle=True)
    # print("이미 존재하는 FAISS 인덱스 및 레이블 파일을 불러왔습니다.")
else:
    # 존재하지 않으면 임베딩을 생성하고 저장
    emotion_embeddings = []
    for idx, emotion in enumerate(emotions_db):
        embedding = embedding_model.embed_query(emotion)
        emotion_embeddings.append(embedding)
        # print(f"{idx + 1}/{len(emotions_db)}: '{emotion}' 임베딩 생성 완료")

    # 감정 단어를 위한 FAISS 인덱스 생성 및 추가
    dimension = len(emotion_embeddings[0])  # 임베딩 차원 수
    faiss_index = faiss.IndexFlatL2(dimension)
    faiss_index.add(np.array(emotion_embeddings).astype("float32"))

    # FAISS 인덱스와 단어 리스트를 로컬에 저장
    faiss.write_index(faiss_index, "emotion_embeddings.index")
    with open("emotion_labels.npy", "wb") as f:
        np.save(f, np.array(emotions_db))


def find_most_similar_word_embedding(target_word, top_n=1):
    input_embedding = np.array(
        [embedding_model.embed_query(target_word)], dtype="float32"
    )

    _, indices = faiss_index.search(input_embedding, top_n)

    top_emotions = [emotion_labels[idx] for idx in indices[0]]
    # print(
    #     f"Most similar word to '{target_word}' is {top_emotions[0]}, distance: {indices[0][0]}"
    # )
    return top_emotions[0]


async def find_emotions_from_sentence(sentence: str) -> List[str]:
    emotions_db_copy = copy.deepcopy(emotions_db)
    result_list = []
    for model_num in range(3):
        random.shuffle(emotions_db_copy)  # emotions_db_copy 랜덤 섞기
        chain = prompt | llms[model_num] | output_parser
        result = await chain.ainvoke(
            {"query": sentence, "emotion_list_with_comma": ",".join(emotions_db_copy)}
        )

        for key, value in result.items():
            if key.startswith("common") or key.startswith("uncommon"):
                if value in emotions_db_copy:
                    result_list.append(value)
                else:
                    print(f"Warning: {value} in {sentence}")
                    pass

        if len(result_list) > 20:
            break

        emotions_db_copy[:] = [
            emotion for emotion in emotions_db_copy if emotion not in result_list
        ]

    return result_list


async def diary_find_emotions(request: List[str]) -> List[DiaryContent]:
    tasks = [find_emotions_from_sentence(content) for content in request]
    results = await asyncio.gather(*tasks)

    content_list = [
        DiaryContent(
            order_index=idx, original_content=content, recommend_emotion=result
        )
        for idx, (content, result) in enumerate(zip(request, results))
    ]

    return content_list
