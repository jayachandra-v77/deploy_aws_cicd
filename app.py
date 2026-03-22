import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Request schema
class Query(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/ask")
def ask(query: Query):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",   # fast + cheap
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query.question}
            ]
        )

        return {
            "answer": response.choices[0].message.content
        }

    except Exception as e:
        return {"error": str(e)}