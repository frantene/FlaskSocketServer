from typing import Dict, List
from datetime import datetime
import random
import uuid


def generate_code(length: int) -> str:
    code: str = ""
    for _ in range(length):
        code += str(random.randint(0, 9))
    return code


class Room:
    def __init__(self) -> None:
        self.rooms: Dict[str, dict] = {}

    def create_room(self, room_name: str, length: int = 8) -> str:
        while True:
            code: str = generate_code(length)
            if code not in self.rooms:
                break
        room_data: Dict[str, List] = {
            'RoomName': room_name,
            'MembersList': {},
            'MessageHistory': []
        }
        self.rooms.update({code: room_data})
        return code

    def delete_room(self, room_code: str) -> None:
        del self.rooms[room_code]

    def add_player(self, code: str, username: str) -> str:
        user_uuid: str = uuid.uuid4().__str__()
        self.rooms[code]['MembersList'][user_uuid] = username
        return user_uuid

    def remove_player(self, code: str, player_uuid: str) -> None:
        del self.rooms[code]['MembersList'][player_uuid]
        if len(self.rooms[code]['MembersList']) <= 0:
            self.delete_room(code)

    def get_player_name(self, code: str, player_uuid: str) -> str:
        return self.rooms[code]['MembersList'][player_uuid]

    def add_message(self, code: str, player_uuid: str, message) -> dict:
        message_metadata: Dict[str, str] = {
            'PlayerName': self.get_player_name(code, player_uuid),
            'Message': message,
            'Time': datetime.now().strftime("%I:%M:%S %p")
        }
        self.rooms[code]['MessageHistory'].append(message_metadata)
        return message_metadata

    def get_message_history(self, code: str) -> list:
        return self.rooms[code]['MessageHistory']

    def room_exist(self, code: str) -> bool:
        if self.rooms.get(code) is not None:
            return True
        else:
            return False

    def room_member_exist(self, code: str, player_uuid: str) -> bool:
        if self.rooms[code]['MembersList'].get(player_uuid, False):
            return True
        else:
            return False
