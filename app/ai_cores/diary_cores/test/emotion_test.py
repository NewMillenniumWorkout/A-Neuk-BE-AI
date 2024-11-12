from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
from sklearn.metrics.pairwise import cosine_similarity
import faiss
import numpy as np
import openai
import dotenv

dotenv.load_dotenv()

# OpenAI 임베딩 모델 설정
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")

# # emotions.txt 파일에서 감정 단어를 읽어오기
# with open('emotions.txt', 'r', encoding='utf-8') as f:
#     emotions = [line.strip() for line in f.readlines()]

# # 감정 단어 임베딩 생성
# emotion_embeddings = []
# for idx, emotion in enumerate(emotions):
#     embedding = embedding_model.embed_query(emotion)
#     emotion_embeddings.append(embedding)
#     print(f"{idx + 1}/{len(emotions)}: '{emotion}' 임베딩 생성 완료")

# # 감정 단어를 위한 FAISS 인덱스 생성 및 추가
# dimension = len(emotion_embeddings[0])  # 임베딩 차원 수
# faiss_index = faiss.IndexFlatL2(dimension)
# faiss_index.add(np.array(emotion_embeddings).astype('float32'))

# # FAISS 인덱스와 단어 리스트를 로컬에 저장
# faiss.write_index(faiss_index, 'emotion_embeddings.index')
# with open('emotion_labels.npy', 'wb') as f:
#     np.save(f, np.array(emotions))

# FAISS 인덱스 및 단어 리스트 로드
faiss_index = faiss.read_index('emotion_embeddings.index')
emotion_labels = np.load('emotion_labels.npy', allow_pickle=True)

# 코사인 유사도 기반 상위 n개 단어 추출 함수
def find_top_emotion_words(input_text, top_n=10):
    # 입력 문장의 임베딩 생성
    input_embedding = np.array([embedding_model.embed_query(input_text)], dtype='float32')

    # FAISS를 사용하여 유사도가 가장 높은 단어 인덱스 찾기
    _, indices = faiss_index.search(input_embedding, top_n)

    # 상위 n개의 감정 단어 반환
    top_emotions = [emotion_labels[idx] for idx in indices[0]]
    return top_emotions

if __name__ == "__main__":
    # 사용자 입력을 통해 테스트 문장 받기
    while True:
        input_text = input("감정을 분석할 문장을 입력하세요: ")
        top_emotions = find_top_emotion_words(input_text)
        print("유사한 감정 단어 상위 5개:", top_emotions)