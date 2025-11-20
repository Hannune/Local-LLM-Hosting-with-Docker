# server.py

from fastapi import FastAPI
from fastapi.responses import StreamingResponse, JSONResponse
from interpreter import interpreter
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

interpreter.llm.model = os.getenv("MODEL_NAME")
interpreter.llm.api_base = os.getenv("OPENAI_API_BASE")
interpreter.llm.api_key = os.getenv("OPENAI_API_KEY")
interpreter.llm.max_tokens = int(os.getenv("MAX_TOKENS", 3000))
interpreter.llm.context_window = int(os.getenv("CONTEXT_WINDOW", 8000))

# interpreter.system_message += """
# If you need to install any necessary packages, use python3 -m venv venv to create new virtual environment."""
interpreter.auto_run = True
interpreter.verbose = os.getenv("VERBOSE")

@app.get("/chat")
def chat_endpoint(message: str):
    """
    Returns the complete response once Open Interpreter finishes processing.
    """
    full_response = ""
    for chunk in interpreter.chat(message, stream=False):
        full_response += str(chunk)
    return JSONResponse({
        "message": message,
        "response": full_response,
        "status": "completed"
    })

@app.get("/chat_stream")
def chat_stream_endpoint(message: str):
    """
    Streams responses in real time (if you still want streaming).
    """
    def event_stream():
        for chunk in interpreter.chat(message, stream=True):
            yield f"data: {chunk}\n\n"
    return StreamingResponse(event_stream(), media_type="text/event-stream")

@app.get("/history")
def history_endpoint():
    return interpreter.messages