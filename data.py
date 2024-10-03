import json
import random

import room
import character

with open('gamedata.json', 'r') as f:
    gamedata = json.load(f)


def createRooms() -> list[room.Room]:
    """Must follow order of room: Dungeon, Kitchen, Hall, Toilet, Bedroom
    Store Name & Number of enemies
    """

    list_of_rooms = []
    for name, roomdata in gamedata.items():
        temp = room.Room(name)
        for _ in range(roomdata["num_enemies"]):
            temp.add_enemy(character.Soldier(20))
        list_of_rooms.append(temp)
    temp.add_enemy(character.Princess(1))

    return list_of_rooms

def createPlayer() -> character.Player:
    record = gamedata["player"]
    return character.Player(record["hp"], record["str"])

def createPrincess() -> character.Princess:
    record = gamedata["princess"]
    return character.Princess(record["hp"])

def createSoldier() -> character.Soldier:
    record = gamedata["soldier"]
    min_str, max_str = record["str"]
    return character.Soldier(record["hp"], random.randint(min_str, max_str))