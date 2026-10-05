"""Local LLM chat server: llama.cpp model + streaming API + static chat page."""
import json
import os

from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from llama_cpp import Llama
from pydantic import BaseModel

MODEL_PATH = os.environ.get("MODEL_PATH", "models/qwen2.5-1.5b-instruct-q4_k_m.gguf")

llm = Llama(model_path=MODEL_PATH, n_ctx=4096, n_threads=os.cpu_count(), verbose=False)
app = FastAPI()


class ChatRequest(BaseModel):
    messages: list[dict]
    temperature: float = 0.7
    max_tokens: int = 512


@app.get("/")
def index():
    return FileResponse("static/index.html")


@app.post("/api/chat")
def chat(req: ChatRequest):
    stream = llm.create_chat_completion(
        messages=req.messages,
        temperature=req.temperature,
        max_tokens=req.max_tokens,
        stream=True,
    )

    def events():
        for chunk in stream:
            token = chunk["choices"][0]["delta"].get("content")
            if token:
                yield f"data: {json.dumps(token)}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(events(), media_type="text/event-stream")
