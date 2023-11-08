from SideQuest_CS_Week3.chatroom.API import Message
from SideQuest_CS_Week3.chatroom.API import Room
import SideQuest_CS_Week3.chatroom.API as API


mess = Message(body="Hello, World!", author="John")
room = Room(id="prout", messages=[])


API.create_room("prout")
API.send_message("prout", mess)
print(API.get_chat("prout"))