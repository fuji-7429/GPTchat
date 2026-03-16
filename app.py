from openai import OpenAI
import streamlit as st

client = OpenAI()

prompt_text = st.text_area("質問を入力してください")

if prompt_text:
    response = client.chat.completions.create(
        model = "gpt-5-nano",
        messages=[
            {"role": "user",
            "content": prompt_text},
        ],
    )

    # print(response.choices[0].message.content)
    st.write(response.choices[0].message.content)



