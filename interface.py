import script
import room
import ctps

class Interface:
    def __init__(self):
        self.func_map = {
            "Dungeon": self.dungeon_menu,
            "Kitchen": self.kitchen_menu,
            "Hall": self.hall_menu,
            "Toilet": self.toilet_menu,
            "Bedroom": self.bedroom_menu
        }

    def prompt(self):
        return script.prompt

    def start_menu(self):
        print(script.start_menu['title'])
        [print(f"{num+1}: {value}") for num, value in enumerate(script.start_menu["options"])]
        choice = int(input(script.prompt))
        return script.start_menu['options'][choice - 1]

    def combat_menu(self):
        print(f"Your health: {ctps.get_player_health()}")
        print(f"Enemy health: {room.get_enemy_health()}")
        
    def dungeon_menu(self):
        [print(f"{num+1}: {value}") for num, value in enumerate(script.dungeon_menu["options"])]
        choice = int(input(script.prompt))
        return script.dungeon_menu['options'][choice - 1]

    def kitchen_menu(self):
        [print(f"{num+1}: {value}") for num, value in enumerate(script.kitchen_menu["options"])]
        choice = int(input(script.prompt))
        return script.kitchen_menu['options'][choice - 1]


    def hall_menu(self):
        [print(f"{num+1}: {value}") for num, value in enumerate(script.hall_menu["options"])]
        choice = int(input(script.prompt))
        return script.hall_menu['options'][choice - 1]

    def toilet_menu(self):
        [print(f"{num+1}: {value}") for num, value in enumerate(script.toilet_menu["options"])]
        choice = int(input(script.prompt))
        return script.toilet_menu['options'][choice - 1]

    def bedroom_menu(self):
        [print(f"{num+1}: {value}") for num, value in enumerate(script.bedroom_menu["options"])]
        choice = int(input(script.prompt))
        return script.bedroom_menu['options'][choice - 1]


    def exit_screen(self):
        print(script.exit_screen['message'])

