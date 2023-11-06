from API import Message
from API import Room
import API


mess = Message(body="Hello, World!", author="John")
room = Room()

API.send_message(mess, room)
print(API.get_chat(room))