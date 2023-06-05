import openai

def ask(api ,A:str):
    openai.api_key = api
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "너는 논리식을 받을거야 너는 받은 논리식을 논리표로 분석해서 논리표를 보여주면서 타당성과 이유를 간단하게 말해줘 (논리표 작성 시 True면 T False면 F로 표기해줘)"},
            {"role": "user", "content": A}
        ]
    )
    answer = response.choices[0].message.content.strip()
    return answer