# backend/main.py 行ごとの詳細解説
## import・設定まわり
from fastapi import FastAPI

FastAPI のアプリ本体を作るためのクラスを読み込む。

from pydantic import BaseModel

リクエストBody（JSON）の型構造を定義するために使う。

from openai import OpenAI

ChatGPT（OpenAI API）を呼び出すためのクライアントクラス。

from fastapi.middleware.cors import CORSMiddleware

ブラウザ（Streamlit）から API を呼び出すための CORS 対策用ミドルウェア。


## リクエストデータ定義
class Prompt(BaseModel):

FastAPI が受け取る JSON の構造を定義するクラス。

text: str

{"text": "質問文"} という形式の JSON を受け取ることを意味する。


## FastAPI アプリ作成
app = FastAPI()

FastAPI サーバー本体のインスタンスを作成。


## CORS 設定
app.add_middleware(...)

フロントエンド（Streamlit）からの通信を許可する設定。

allow_origins=["*"]

全てのアクセス元を許可（開発用設定）。

allow_credentials=True

Cookie や認証情報の送信を許可。

allow_methods=["*"]

GET / POST など全ての HTTP メソッドを許可。

allow_headers=["*"]

全ての HTTP ヘッダーを許可。


## OpenAI クライアント
client = OpenAI()

ChatGPT API を呼び出すためのクライアントを生成。


## API エンドポイント
@app.post("/chat")

/chat という URL に対する POST リクエストを受け付ける。

## 
def chat_with_ai(prompt: Prompt):

受け取った JSON を Prompt 型として受信する関数。


## ChatGPT 呼び出し
response = client.chat.completions.create(...)

ChatGPT に質問を送信し、回答を取得する処理。

model="gpt-5-nano"

使用する ChatGPT のモデルを指定。

messages=[{"role": "user", "content": prompt.text}]

ユーザーが入力した文章を ChatGPT に渡す。


## 結果の取り出し・返却
answer = response.choices[0].message.content

## ChatGPT の返答テキストを取り出す。

return {"answer": answer}

JSON レスポンスとしてフロントエンドに返却。


# frontend/app.py 行ごとの詳細解説
## import・定数定義
import streamlit as st

Streamlit の UI 部品を使うための import。

import requests

FastAPI に HTTP リクエストを送るためのライブラリ。

## 
API_URL = "http://localhost:8000/chat"

バックエンド API の URL を定義。


## UI 表示
st.title("チャットAIアプリ（FastAPI + Streamlit）")

Web画面のタイトルを表示。

## 
prompt_text = st.text_area("質問を入力してください")

ユーザーが文章を入力するテキストエリア。
入力内容は prompt_text に入る。


## ボタン処理
if st.button("送信"):

「送信」ボタンが押されたときのみ処理を実行。

## 
if not prompt_text.strip():

入力が空（または空白のみ）かどうかをチェック。

st.warning("質問を入力してください")

入力がない場合、警告メッセージを表示。


## API 呼び出し
with st.spinner("AIが回答を生成中..."):

ChatGPT の処理中にスピナー（ローディング表示）を出す。

## 
response = requests.post(API_URL, json={"text": prompt_text})

FastAPI に対して JSON をつけて POST リクエストを送信。


## 結果表示
if response.status_code == 200:

FastAPI が正常に応答した場合の処理。

answer = response.json()["answer"]

返却された JSON から回答テキストを取り出す。

st.write("### 回答：")

回答用の見出しを表示。

st.write(answer)

ChatGPT の回答を画面に表示。


## エラー処理
else:

API がエラーを返した場合。

st.error("APIエラーが発生しました")

エラーメッセージを赤色で表示。