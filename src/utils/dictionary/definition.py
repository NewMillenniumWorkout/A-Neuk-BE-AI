import requests
import os
import dotenv
import xml.etree.ElementTree as ET

if __name__ == '__main__':
    # .env 파일에서 API_KEY 로드
    dotenv.load_dotenv("../../../.env")
    API_KEY = os.environ.get('DICTIONARY_API_KEY')
    API_URL = 'https://krdict.korean.go.kr/api/search'

    # 감정 단어 파일 읽기
    with open('emotions.txt', 'r', encoding='utf-8') as f:
        emotion_words = [line.strip() for line in f if line.strip()]

    # 결과 저장 파일
    output_file = 'emotion_words_with_meaning.txt'

    def get_word_meaning(word):
        """
        API를 호출하여 단어의 뜻을 가져오는 함수 (XML 응답 처리)
        """
        params = {
            'key': API_KEY,
            'q': word,
            'type_search': 'search',
            'part': 'word',
            'sort': 'dict',
        }
        try:
            response = requests.get(API_URL, params=params)
            response.raise_for_status()
            root = ET.fromstring(response.text)

            # XML 파싱: 첫 번째 <item>의 <sense> 내 <definition> 태그
            item = root.find("item")
            if item is not None:
                sense = item.find("sense")
                if sense is not None:
                    definition = sense.find("definition")
                    if definition is not None:
                        return definition.text.strip()
            return "뜻을 찾을 수 없음"
        except Exception as e:
            print(f"Error for word '{word}': {e}")
            return "뜻을 찾을 수 없음"

    # 결과 저장
    with open(output_file, 'w', encoding='utf-8') as f:
        for word in emotion_words:
            meaning = get_word_meaning(word)
            f.write(f"{word}\t{meaning}\n")
            print(f"Processed: {word}")

    print(f"결과가 '{output_file}' 파일에 저장되었습니다.")
