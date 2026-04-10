from openai import OpenAI
import streamlit as st

## 初期設定
# ページの横いっぱいに表示されるけど、なんか違う
st.set_page_config(layout="wide")
client = OpenAI()
if "questions" not in st.session_state:
    st.session_state.questions = []

## 関数作成
def make_user_assistant_pairs(messages):
    pairs = []
    current_user = None

    for msg in messages:
        # msg["role"]でもいいが、チャットログにroleキーが無かったらエラーを吐いてしまう
        # msg.get("role")なら、キーが無くてもNoneを返すだけで止まらないので、適切
        role = msg.get("role") 
        content = msg.get("content")

        if role == "user":
            current_user = content
        elif role == "assistant" and current_user:
            pairs.append((current_user, content))
            current_user = None
    return pairs


## 将来拡張用
## user:systemを導入
if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = "あなたは親切なアシスタントです。"




## サイドバー
with st.sidebar:
    columns_ratio= st.slider("カラム幅比率", 0.05, 0.95, 0.25, 0.05)



## メインページ出力
st.title("ChatGPT")
st.markdown("---")

col1, col2 = st.columns([columns_ratio, 1-columns_ratio])

with col1:
    # 質問履歴を一覧として表示
    with st.container(border=True):
        st.write("過去質問一覧")

        # 関数を使わない場合
        # pairs = []
        # current_user = None

        # for msg in st.session_state.questions:
        #     role = msg["role"]
        #     content = msg["content"]

        #     if role == "user":
        #         current_user = content
        #     elif role == "assistant" and current_user is not None:
        #         pairs.append((current_user, content))
        #         current_user = None
        # 関数を使う場合
        pairs = make_user_assistant_pairs(st.session_state.questions)

        for user, assistant in pairs:
            # if len(user) < 20:
            #     with st.expander(user):
            #         st.write(f">{user}")
            #         st.write(assistant)
            # else:
            #     with st.expander(f"{user[:20]}..."):
            #         st.write(f">{user}")
            #         st.write(assistant)   
            # 別表記
            title = user if len(user) < 20 else f"{user[:20]}..."
            with st.expander(title):
                st.write(f"> {user}")
                st.write(assistant)




with col2:
    # ChatAI本体
    st.subheader("ChatAI")

    with st.form("chat_form", border=False):
        prompt_text = st.text_area(
            "質問を入力してください", 
            placeholder="Ctrl + Enter で送信"
            )
        submitted = st.form_submit_button("送信")

    if submitted and prompt_text:
        st.session_state.questions.append({"role": "user", "content": prompt_text})
        messages = [{"role": "system", "content": st.session_state.system_prompt}]
        messages += st.session_state.questions

        response = client.chat.completions.create(
            model = "gpt-5-nano",
            messages = messages
        )

        try:
            answer = response.choices[0].message.content
        except Exception as e:
            answer = f"エラーが発生しました: {e}"
        st.write(answer)

        st.session_state.questions.append({"role": "assistant", "content": answer})

