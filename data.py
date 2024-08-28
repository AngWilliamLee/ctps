import json

import room
import character


def createRooms() -> list[room.Room]:
    """Must follow order of room: Dungeon, Kitchen, Hall, Toilet, Bedroom
    Store Name & Number of enemies
    """

    list_of_rooms = []
    room_name_enemy_num = {
        "Dungeon": 3,
        "Kitchen": 3,
        "Hall": 3,
        "Toilet": 3,
        "Bedroom": 3
    }
    for name, num in room_name_enemy_num.items():
        temp = room.Room(name)
        for _ in range(num):
            temp.add_enemy(character.Soldier(20))
        list_of_rooms.append(temp)
    temp.add_enemy(character.Princess(1))

    return list_of_rooms


with open('data.json', 'r') as f:
    char_data = json.load(f)


def createPlayer() -> character.Player:
    """
    
    """
    record = char_data["player"]
    return character.Player(record["hp"], record["str"])


def createPrincess() -> character.Princess:
    record = char_data["princess"]
    return character.Princess(record["hp"])
