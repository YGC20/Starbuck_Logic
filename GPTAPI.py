import openai

openai.api_key = "API_Cod"

# ChatGPT API 요청 보내기
# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You will now receive a sentence of propositional logic. When you receive a sentence of propositional logic, distinguish true from false and ask for an interpretation of the result."},
#         {"role": "user", "content": }
#     ]
# )

# 응답 확인
# print(response.choices[0].message.content)

def ask(A:str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "너는 논리식을 받을거야 너는 받은 논리식을 논리표로 분석해서 논리표를 보여주면서 타당성을 말해줘"},
            {"role": "user", "content": A}
        ]
    )
    answer = response.choices[0].message.content
    return answer

