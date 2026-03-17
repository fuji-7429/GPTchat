from openai import OpenAI
import streamlit as st
# import time

## 初期設定
# ページの横いっぱいに表示されるけど、なんか違う
st.set_page_config(layout="wide")
client = OpenAI()

## 関数定義
# 文章をゆっくり出力するやつ(AIの順次出力するやつ)
# 重いため却下
# def response_generator(text):
#     for word in text.split():
#         yield word + ""
#         time.sleep(0.05)


## メインページ出力
# チャットメッセージのコンテナ
# with st.chat_message("user"):
#         st.write("Hello")
    
# チャット入力ウィジットで、メッセージ入力が可能
# prompt = st.chat_input("Say samting")
# if prompt:
#     st.write(f"君の発言内容:{prompt}")

## チャットアプリの本格実装
# チャット履歴を順番に表示
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 質問し、それを表示&保存する
if prompt := st.chat_input("どうした？"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

# 返答を出力し保存する
    # response = f"Echo: {prompt}"
    # with st.chat_message("assistant"):
    #     st.markdown(response)

    # st.session_state.messages.append({"role": "assistant", "content": response})

# リアルタイム出力っぽく出力することができるが、遅い
    # with st.chat_message("assistant"):
    #     st.write_stream(response_generator(response))

# 生成AIの出力
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
                model = "gpt-5-nano",
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                # チャンクごとにリアルタイムで出力される
                # チャンクで別れるため、出力形式を変える必要がある
                # stream=True, 
                )
        # stream=Trueの時
        # response = st.write_stream(stream)
        # stream=False(デフォルト)の時
        response = stream.choices[0].message.content
        st.write(response)
        
    st.session_state.messages.append({"role": "assistant", "content": response})

