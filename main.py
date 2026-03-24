import streamlit as st

chatai_selfmade = st.Page(page="contents/app.py", title="自作チャットAI", icon=":material/chat:")
chatai_fromst   = st.Page(page="contents/app2.py", title="st公式チャットAI", icon=":material/chat:")

pg = st.navigation([chatai_selfmade, chatai_fromst])
pg.run()

