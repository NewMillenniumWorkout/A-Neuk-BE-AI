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
import time


with open("emotions.txt", "r", encoding="utf-8") as f:
    emotions_db = [line.strip() for line in f.readlines()]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")

output_parser = JsonOutputParser(pydantic_object=DiaryEmotionList)
format_instructions = output_parser.get_format_instructions()

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
    random.shuffle(emotions_db)
    chain = prompt | llm | output_parser
    result = await chain.ainvoke(
        {"query": sentence, "emotion_list_with_comma": ",".join(emotions_db)}
    )
    result_list = []
    for key, value in result.items():
        if key.startswith("common") or key.startswith("uncommon"):
            if value in emotions_db:
                result_list.append(value)
            else:
                # result_list.append(find_most_similar_word_embedding(value)) # 임베딩 기반 검색
                pass
    return result_list


async def diary_find_emotions(request: List[str]) -> List[DiaryContent]:
    start_time = time.time()

    # 각 입력 문장에 대해 비동기 작업 생성
    tasks = [find_emotions_from_sentence(content) for content in request]
    results = await asyncio.gather(*tasks)

    content_list = [
        DiaryContent(
            order_index=idx, original_content=content, recommend_emotion=result
        )
        for idx, (content, result) in enumerate(zip(request, results))
    ]

    end_time = time.time()
    print(f"diary_find_emotions executed in {end_time - start_time:.2f} seconds.")
    return content_list
