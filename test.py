from utilities.function import Room
# import pprint
import json


room = Room()

code = room.create_room("Hello")

room.add_player(code, "GamerVerse")
room.add_player(code, "AmongUs")

code = room.create_room("Nerds")
uuid1 = room.add_player(code, "Brody")
uuid2 = room.add_player(code, "Taiden")

room.add_message(code, uuid1, "Hello Room Nerds")
room.add_message(code, uuid2, "No")

data = json.dumps(room.rooms, indent=4)
open('sample.json', 'w').write(data)
