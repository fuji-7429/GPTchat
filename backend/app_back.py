from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware

class Prompt(BaseModel):
    text: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI()

@app.post("/chat")
def chat_with_ai(prompt: Prompt):
    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role": "user", "content": prompt.text}
        ]
    )
    answer = response.choices[0].message.content
    return {"answer": answer}