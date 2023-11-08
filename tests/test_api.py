from fastapi.testclient import TestClient  

from chatroom import API  #on import la var global app
from chatroom.API import app  #on import la var global app
from chatroom.API import rooms

from chatroom.API import Message
#from SideQuest_CS_Week3.chatroom.API import Room
#import SideQuest_CS_Week3.chatroom.API as API


client = TestClient(app)

def test_root_not_found():
    response = client.get("/")
    assert response.status_code == 404

def test_send_message_no_room(room_id = "prout", body = "hello", author = "jean"): 
    response = client.post("/chat/{room_id}/send",
                            json={"body": body, "author": author})
    assert response.status_code == 200
    assert response.json() ==  f"La room n'existe pas"    #car on a pas encore créée la room 
    

def test_create_room(room_id = "prout"):
    response = client.post("/chat/create/{room_id}")
    assert response.status_code == 200
    assert response.json() == "room created" 


def test_send_message(room_id = "prout", body = "hello", author = "jean"):  #garde en compte que la room a été crée avec le precedent test #FAUXX
    API.create_room(room_id)
    response = client.post(f"/chat/{room_id}/send",
                            json={"body": body, "author": author})
    assert response.status_code == 200
    assert response.json() ==  f"message send to chatroom {room_id}"



