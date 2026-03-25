## 本当はタブ切り替えなどで履歴だけを見れるようにしたかったが、
## st.chat_inputのバグで、タブなどに入れると最下部から移動してしまうらしい
## なので、このアプリではチャット機能のみを実装


from openai import OpenAI
import streamlit as st

## 初期設定
# レイアウトをサイドバーで設定できるようにするための事前準備
if "layout" not in st.session_state:
    st.session_state.layout = "centered"
# ページの横いっぱいに表示する
st.set_page_config(layout=st.session_state.layout)
client = OpenAI()



## サイドバーによる設定
with st.sidebar:
    layout = st.toggle("Wideモードにする")
    new_layout = "wide" if layout else "centered"
    if new_layout != st.session_state.layout:
        st.session_state.layout = new_layout
        st.rerun() # ページの再読み込み(再起動とは違う)
        
    st.markdown("---")
    use_stream = st.toggle("ストリーミング出力ON/OFF")



## チャットアプリの本格実装
st.title("ChatGPT")
st.markdown("---")

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
                stream=use_stream, 
                )
        if use_stream:
            response = st.write_stream(stream)
        else:
            response = stream.choices[0].message.content
        st.write(response)
        
    st.session_state.messages.append({"role": "assistant", "content": response})

