# chat_app.py
# http://127.0.0.1:8000/docs#

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Dict

app = FastAPI()

class Message(BaseModel):
    body: str
    author: str

class Room(BaseModel):
    id: str
    messages: list[Message]

rooms = []  #list[Room]

@app.post("/chat/create/{room_id}")
def create_room(room_id: str):
    rooms.append(Room(id= room_id, messages= []))
    return "room created"

@app.get("/chat/{room_id}")
def get_chat(room_id: str):
    for room in rooms:
        if room_id == room.id:
            c_room = room                                                                          
    return c_room.messages

@app.post("/chat/{room_id}/send")
def send_message(room_id: str, message: Message):
    for room in rooms:
        if room_id == room.id:
            c_room = room  

    timestamp = datetime.now()
    #chat_message = {
    #    "body": message.body,
    #    "author": message.author,
    #    "date": timestamp
    #}
    c_room.messages.append(message)  
    return f"message send to chatroom {c_room.id}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
