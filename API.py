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
   # date : datetime

class Room():
    def __init__(self) -> None:
        #self.app = FastAPI()
        self.messages =[]

@app.get("/chat")
def get_chat(room: Room):
    return room.messages

@app.post("/chat")
def send_message(message: Message, room: Room):
    timestamp = datetime.now()
    chat_message = {
        "body": message.body,
        "author": message.author,
        "date": timestamp
    }
    room.messages.append(chat_message)
    return chat_message

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
