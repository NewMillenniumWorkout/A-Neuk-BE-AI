from typing import List
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from app.models.diary_models import DairyStrList, LLMError

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

output_parser = JsonOutputParser(pydantic_object=DairyStrList)
format_instructions = output_parser.get_format_instructions()

examples = [
    {
        "input": "아침에 마신 커피가 정말 맛있었다. 그 향과 맛이 시작부터 기분 좋게 해줬다. 오늘 점심으로는 스파게티를 먹었는데, 역시나 맛있었다. 점심 후에는 팀원들과 함께 오픈소스 데모 데이터를 준비했다. 다들 기대 반, 걱정 반으로 분위기가 묘했다. 긴장도 되지만, 잘 해낼 것 같은 느낌이 든다. 데모 데이가 끝나면 뭘 할지 아직 정하지 않았지만, 아마도 조금 쉬어야겠다. 오늘 하루가 어떻게 마무리될지 기대가 된다.",
        "output": """{{
            "content": [
                "아침에 마신 커피가 정말 맛있었다. 그 향과 맛이 시작부터 기분 좋게 해줬다.",
                "오늘 점심으로는 스파게티를 먹었는데, 역시나 맛있었다.",
                "점심 후에는 팀원들과 함께 오픈소스 데모 데이터를 준비했다. 다들 기대 반, 걱정 반으로 분위기가 묘했다. 긴장도 되지만, 잘 해낼 것 같은 느낌이 든다.",
                "데모 데이가 끝나면 뭘 할지 아직 정하지 않았지만, 아마도 조금 쉬어야겠다. 오늘 하루가 어떻게 마무리될지 기대가 된다."
            ]
        }}""",
    },
    {
        "input": "오늘 드디어 새로 산 맥북이 도착했다. 박스를 열 때부터 두근두근 설레는 마음을 감출 수 없었어. 맥북을 손에 들었을 때, 정말 예쁘고 고급진 디자인에 감탄했다. 화면을 켜니 선명하고 깔끔한 디스플레이가 눈에 들어왔고, 타이핑을 할 때마다 손끝에서 느껴지는 촉감도 너무 좋았다. 이제 이 맥북으로 세팅을 마치고, 내가 계획한 코딩 프로젝트를 시작해야겠다. 새로운 환경에서 작업하는 게 처음이라 조금 긴장되긴 하지만, 동시에 기대도 많이 된다. 오늘은 하루 종일 맥북 세팅하고, 필요한 프로그램들을 설치하면서 시간을 보냈다. 작은 문제들도 있었지만, 하나하나 해결해 나가면서 새 장비에 적응해갔다. 앞으로 이 맥북과 함께할 나의 코딩 여정이 무척 기대된다. 열심히 해야지",
        "output": """{{
            "content": [
                "오늘 드디어 새로 산 맥북이 도착했다. 박스를 열 때부터 두근두근 설레는 마음을 감출 수 없었어. 맥북을 손에 들었을 때, 정말 예쁘고 고급진 디자인에 감탄했다.",
                "화면을 켜니 선명하고 깔끔한 디스플레이가 눈에 들어왔고, 타이핑을 할 때마다 손끝에서 느껴지는 촉감도 너무 좋았다.",
                "이제 이 맥북으로 세팅을 마치고, 내가 계획한 코딩 프로젝트를 시작해야겠다. 새로운 환경에서 작업하는 게 처음이라 조금 긴장되긴 하지만, 동시에 기대도 많이 된다.",
                "오늘은 하루 종일 맥북 세팅하고, 필요한 프로그램들을 설치하면서 시간을 보냈다. 작은 문제들도 있었지만, 하나하나 해결해 나가면서 새 장비에 적응해갔다.",
                "앞으로 이 맥북과 함께할 나의 코딩 여정이 무척 기대된다. 열심히 해야지"
            ]
        }}""",
    },
    {
        "input": "오늘은 평소와 다름없는 하루였다. 아침에 일어나서 알바를 갔는데, 다행히 오늘은 일이 적어서 덜 힘들었다. 요즘 알바가 꽤 힘들었는데, 오늘은 조금 여유가 있어서 다행이라는 생각이 들었다.  알바를 마치고 집에 와서는 과제를 했다. 과제는 거의 마무리 단계에 있어서 큰 부담은 없었다. 제출도 다 끝내서 마음이 한결 가벼워졌다. 이제 남은 건 다른 조의 과제를 리뷰하는 일인데, 이 부분도 그렇게 어렵진 않을 것 같다. 그래도 빨리 끝내고 싶다.  오늘은 특별한 일이 없었지만, 그래도 일이 적어서 조금은 여유로운 하루였다. 과제도 거의 끝나가니 마음이 조금 놓인다. 내일도 무사히 하루를 보내길 바라면서, 오늘 하루를 마무리한다.",
        "output": """{{
            "content": [
                "오늘은 평소와 다름없는 하루였다. 아침에 일어나서 알바를 갔는데, 다행히 오늘은 일이 적어서 덜 힘들었다.",
                "요즘 알바가 꽤 힘들었는데, 오늘은 조금 여유가 있어서 다행이라는 생각이 들었다.",
                "알바를 마치고 집에 와서는 과제를 했다. 과제는 거의 마무리 단계에 있어서 큰 부담은 없었다. 제출도 다 끝내서 마음이 한결 가벼워졌다.",
                "이제 남은 건 다른 조의 과제를 리뷰하는 일인데, 이 부분도 그렇게 어렵진 않을 것 같다. 그래도 빨리 끝내고 싶다.",
                "오늘은 특별한 일이 없었지만, 그래도 일이 적어서 조금은 여유로운 하루였다. 과제도 거의 끝나가니 마음이 조금 놓인다.",
                "내일도 무사히 하루를 보내길 바라면서, 오늘 하루를 마무리한다."
            ]
        }}""",
    },
]

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Input:\n{input}\n\nOutput:\n{output}\n",
)

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="### User Diary Input:\n{query}\n\n### JSON Output:\n",
    input_variables=["query"],
)

prompt = PromptTemplate(
    template="입력된 문단을 보고 다음의 작업을 수행해 주세요:\n1. **입력된 문단은 사용자의 하루에 대한 일기입니다.**\n2. 일기 내용을 **변형하지 말고**, 각각의 작은 주제를 기준으로 일기를 분리합니다. 각 주제는 하나의 독립적인 활동이나 경험을 포함해야 합니다.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": format_instructions},
)


def diary_split(request: str) -> List[str]:
    chain = {"query": few_shot_prompt} | prompt | llm | output_parser

    try:
        result = chain.invoke({"query": request})
        if result["content_list"] is None:
            raise LLMError()
        return result["content_list"]
    except Exception as e:
        raise LLMError("Failed to split the diary content.")
