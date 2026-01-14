import os

from dotenv import load_dotenv
from fastapi import FastAPI
from google import genai
from pydantic import BaseModel

from data import documents
from vector_store import add_document, query_document

app = FastAPI()

load_dotenv()
key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=key)


class Query(BaseModel):
    question: str


@app.post("/ask")
async def ask_question(query: Query):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=query.question
    )
    print(response.text)


@app.on_event("startup")
def load_data():
    add_document(documents)


@app.get("/search")
def search_docs(q: str):
    result = query_document(q)
    context_text = "\n".join(result)
    prompt = f"""Answer the question using only this context:{context_text} Question: {q}If the context doesn't have the answer, say "I don't know".Answer:"""
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    return {"question": q, "answer": response.text, "context": result}
