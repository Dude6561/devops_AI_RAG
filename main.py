from fastapi import FastAPI
from pydantic import BaseModel
import os
from google import genai
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=key)

app = FastAPI()

class Query(BaseModel):
    question:str

@app.post("/ask")
async def ask_question(query: Query):
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=query.question
   )
    print(response.text)

