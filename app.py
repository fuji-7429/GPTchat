from openai import OpenAI
import streamlit as st

## 初期設定
# ページの横いっぱいに表示されるけど、なんか違う
st.set_page_config(layout="wide")
client = OpenAI()
if "questions" not in st.session_state:
    st.session_state.questions = {}



## メインページ出力
st.title("ChatGPT")
st.markdown("---")

col1, col2 = st.columns([1, 3])

with col1:
    with st.container(border=True):
        st.write("過去質問一覧")

        for key,value in st.session_state.questions.items():
            if len(key) < 20:
                with st.expander(key):
                    st.write(f">{key}")
                    st.write(value)
            else:
                with st.expander(f"{key[:20]}..."):
                    st.write(f">{key}")
                    st.write(value)
        # 何も考えず出力するならこちら
        #st.write(st.session_state.questions)


with col2:
    st.subheader("ChatAI")
    prompt_text = st.text_area("質問を入力してください")

    if prompt_text:
        response = client.chat.completions.create(
            model = "gpt-5-nano",
            messages=[
                {"role": "user",
                "content": prompt_text},
            ],
        )

        st.write(response.choices[0].message.content)

        st.session_state.questions[prompt_text] = response.choices[0].message.content


