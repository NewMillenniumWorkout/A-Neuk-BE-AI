# 파일 경로 설정
input_file = "emotions.txt"
output_file = "insert_emotions.sql"

default = """
-- 테이블 생성
CREATE TABLE IF NOT EXISTS emotion (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    category TEXT NOT NULL DEFAULT '기타',
    description TEXT NOT NULL,
    example TEXT
);
"""

if __name__ == "__main__":
    # SQL 파일 생성
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        # 테이블에 INSERT 시작
        outfile.write(default)
        outfile.write("INSERT INTO emotion (title, category, description, example)\nVALUES\n")
        
        # 단어 읽어서 SQL 변환
        lines = infile.readlines()
        for i, line in enumerate(lines):
            line = line.strip()  # 공백 제거
            if line:  # 비어 있지 않은 경우만 처리
                # 탭으로 구분된 단어와 카테고리 분리
                try:
                    print(line)
                    word, category, description, example = line.split("\t")
                except ValueError:
                    print(f"잘못된 형식의 줄: {line}")
                    continue
                
                # SQL 변환
                # sql_line = f"    ('{word}', '{category}', '{description}', '{example}')"
                sql_line = f"UPDATE emotion\nSET example='{example}'\nWHERE title='{word}'\n"
                if i < len(lines) - 1:  # 마지막 줄에만 쉼표 제거
                    # sql_line += ","
                    sql_line += ";"
                sql_line += "\n"
                outfile.write(sql_line)
        
        # 끝에 세미콜론 추가
        outfile.write(";")

    print(f"SQL 파일이 {output_file}에 생성되었습니다.")