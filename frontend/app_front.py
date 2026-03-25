import streamlit as st
import requests

API_URL = "http://localhost:8000/chat"

st.title("チャットAIアプリ（FastAPI + Streamlit）")

prompt_text = st.text_area("質問を入力してください")

if st.button("送信"):
    if not prompt_text.strip():
        st.warning("質問を入力してください")
    else:
        with st.spinner("AIが回答を生成中..."):
            response = requests.post(API_URL, json={"text": prompt_text})
            
            if response.status_code == 200:
                answer = response.json()["answer"]
                st.write("### 回答：")
                st.write(answer)
            else:
                st.error("APIエラーが発生しました")