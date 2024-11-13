from typing import List

from app.models.diary_models import DiaryContent
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
import random
import dotenv
import Levenshtein

dotenv.load_dotenv()


class DiaryEmotionList(BaseModel):
    common_top1: str
    common_top2: str
    common_top3: str
    common_top4: str
    common_top5: str
    uncommon_top1: str
    uncommon_top2: str
    uncommon_top3: str
    uncommon_top4: str
    uncommon_top5: str


with open("emotions.txt", "r", encoding="utf-8") as f:
    emotions_db = [line.strip() for line in f.readlines()]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

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


def find_most_similar_word_levenshtein(target_word: str) -> str:
    distances = [
        (word, Levenshtein.distance(target_word, word)) for word in emotions_db
    ]
    most_similar_word = min(distances, key=lambda x: x[1])
    print(
        f"Most similar word to {target_word} is {most_similar_word[0]}, distance: {most_similar_word[1]}"
    )
    return most_similar_word[0]


def check_valid_emotion(emotion: str) -> bool:
    if emotion in emotions_db:
        return True
    return False


async def find_emotions_from_sentence(sentence: str) -> List[str]:
    random.shuffle(emotions_db)
    chain = prompt | llm | output_parser
    result = await chain.ainvoke(
        {"query": sentence, "emotion_list_with_comma": ",".join(emotions_db)}
    )
    result_list = []
    for key, value in result.items():
        if key.startswith("common") or key.startswith("uncommon"):
            if check_valid_emotion(value):
                result_list.append(value)
            else:
                result_list.append(find_most_similar_word_levenshtein(value))
    return result_list


async def diary_find_emotions(request: List[str]) -> List[DiaryContent]:

    content_list = []
    for idx, content in enumerate(request):
        content_list.append(
            DiaryContent(
                order_index=idx,
                original_content=content,
                recommend_emotion=await find_emotions_from_sentence(content),
            )
        )
    return content_list
