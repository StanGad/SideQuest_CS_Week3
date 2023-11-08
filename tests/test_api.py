from fastapi.testclient import TestClient  

from chatroom import API  #on import la var global app
from chatroom.API import app  #on import la var global app

from chatroom.API import Message
#from SideQuest_CS_Week3.chatroom.API import Room
#import SideQuest_CS_Week3.chatroom.API as API


client = TestClient(app)

def test_root_not_found():
    response = client.get("/")
    assert response.status_code == 404

def test_create_room(room_id = "prout"):
    response = client.post("/chat/create/{room_id}")
    assert response.status_code == 200
    assert response.json() == "room created" 



