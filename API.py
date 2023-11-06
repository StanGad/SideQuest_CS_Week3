# chat_app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# In-memory storage for chat messages
chat_messages = []

class Message(BaseModel):
    body: str
    author: str
    date : datetime

@app.get("/chat")
def get_chat():
    return chat_messages

@app.post("/chat")
def send_message(message: Message):
    timestamp = datetime.now()
    chat_message = {
        "body": message.body,
        "author": message.author,
        "date": timestamp
    }
    chat_messages.append(chat_message)
    return chat_message

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
