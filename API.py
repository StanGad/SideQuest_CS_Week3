# chat_app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Dict

app = FastAPI()

# In-memory storage for chat messages
chat_rooms: Dict[str, list] = {}  # A dictionary to store messages by room name

class Message(BaseModel):
    body: str
    author: str

@app.get("/chat/{room_name}")
def get_chat(room_name: str):
    if room_name not in chat_rooms:
        chat_rooms[room_name] = []  # Create the room if it doesn't exist
    return chat_rooms.get(room_name)

@app.post("/chat/{room_name}")
def send_message(room_name: str, message: Message):
    if room_name not in chat_rooms:
        chat_rooms[room_name] = []  # Create the room if it doesn't exist
    timestamp = datetime.now()
    chat_message = {
        "body": message.body,
        "author": message.author,
        "date": timestamp
    }
    chat_rooms[room_name].append(chat_message)
    return chat_message

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
