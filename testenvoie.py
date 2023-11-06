from API import Message
from API import Room
import API


mess = Message(body="Hello, World!", author="John")
room = Room(id="prout", messages=[])


API.create_room("prout")
API.send_message("prout", mess)
print(API.get_chat("prout"))