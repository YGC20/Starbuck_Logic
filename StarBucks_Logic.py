import streamlit as st
from StarBucks_LST import Logic

with st.sidebar:
    st.markdown('''
**API KEY 발급 방법**
1. https://beta.openai.com/ 회원가입
2. https://beta.openai.com/account/api-keys 접속
3. `create new secret key` 클릭 후 생성된 KEY 복사
    ''')
    value=''
    apikey = st.text_input(label='OPENAI API 키', placeholder='OPENAI API키를 입력해 주세요', value=value)

    if apikey:
        st.markdown(f'OPENAI API KEY: `{apikey}`')

    st.markdown('---')

st.title("스타벅스 논리")
st.subheader("논리식을 입력해주세요.")
st.caption("(괄호와 연산자 사이는 띄어쓰기를 부탁드립니다.)")
Input = st.text_input("ex) coffee and coffee -> coffee or coffee")
if st.button("send"):
    answer , ChangeLogic = Logic(apikey , Input)
    st.write(ChangeLogic)
    st.write(answer)
    st.caption("결과값이 올바르지 않게 나오면 다시 한번 'send'를 눌러주세요.")
else:
    st.write("입력 값이 없습니다.")