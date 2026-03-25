import streamlit as st

## 各ページの設定を st.Page オブジェクトとして定義
# これにより、ファイルパスを一箇所で管理できる
# アイコンは下記サイトのものであれば使用可能
# https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded
chatai_selfmade = st.Page(page="contents/app.py", title="自作チャットAI", icon=":material/chat:")
chatai_fromst   = st.Page(page="contents/app2.py", title="st公式チャットAI", icon=":material/chat:")


## ページを設定
# st.navigation にページリストを渡すことで
pg = st.navigation([chatai_selfmade, chatai_fromst])

# セッション状態に保存で、他のファイルからも参照が可能に
# st.switch_page(st.session_state.pages["hoge"])でページ遷移が可能
st.session_state.pages = {
    "chatai_selfmade": chatai_selfmade,
    "chatai_fromst": chatai_fromst
}


# 実行
pg.run()

