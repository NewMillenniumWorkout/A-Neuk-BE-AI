# 파일 경로 설정
input_file = "../../emotions.txt"
output_file = "insert_emotions.sql"

default = """
-- 테이블 생성
CREATE TABLE IF NOT EXISTS emotion (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    example TEXT
);

"""

if __name__ == "__main__":
    # SQL 파일 생성
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        # 테이블에 INSERT 시작
        outfile.write(default)
        outfile.write("INSERT INTO emotion (title, example)\nVALUES\n")
        
        # 단어 읽어서 SQL 변환
        lines = infile.readlines()
        for i, line in enumerate(lines):
            word = line.strip()  # 공백 제거
            if word:  # 비어 있지 않은 경우만 처리
                sql_line = f"    ('{word}', NULL)"
                if i < len(lines) - 1:  # 마지막 줄에만 쉼표 제거
                    sql_line += ","
                sql_line += "\n"
                outfile.write(sql_line)
        
        # 끝에 세미콜론 추가
        outfile.write(";")

    print(f"SQL 파일이 {output_file}에 생성되었습니다.")
