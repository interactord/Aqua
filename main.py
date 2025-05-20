import os
from flask import Flask, request, jsonify
from pydantic import BaseModel
from asgiref.wsgi import WsgiToAsgi
from typing import List
from wtpsplit import SaT

app = Flask(__name__)

os.environ["TOKENIZERS_PARALLELISM"] = "true"
model_ort = SaT("sat-3l-sm", ort_providers=["CPUExecutionProvider"])

def split_text(text: str) -> List[str]:
    result = list(model_ort.split(text))
    return result

class TextRequest(BaseModel):
    originText: str

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/split", methods=["POST"])
def split_text_get():
    body = request.get_json()
    text = body.get("originText")
    if not text:
        return jsonify({"error": "originText 필드가 필요합니다."}), 400
    result = split_text(text)
    return jsonify({"result": result})

asgi_app = WsgiToAsgi(app)
