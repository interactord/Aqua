import os
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
from wtpsplit import SaT

os.environ["TOKENIZERS_PARALLELISM"] = "true"

model_ort = SaT("sat-3l-sm", ort_providers=["CPUExecutionProvider"])

def split_text(text: str) -> List[str]:
    result = list(model_ort.split(text))
    return result

app = FastAPI()

class TextRequest(BaseModel):
    originText: str

@app.get("/")
async def greetings():
    return "Hello World!"

@app.post("/split")
async def split_text_get(request: Request):
    body = await request.json()
    text = body.get("originText")
    if not text:
        return {"error": "originText 필드가 필요합니다."}
    result = split_text(text)
    return {"result": result}
