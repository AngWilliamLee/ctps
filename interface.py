import script


class Interface:
    def prompt(self):
        return script.prompt

    def start_menu(self):
        print(script.start_menu['title'])

        [print(f"{num+1}: {value}") for num, value in enumerate(script.start_menu["options"])]
        choice = int(input(script.prompt))
        return script.start_menu['options'][choice - 1]

    def combat_menu(self, turn):
        print(f"Your health: {player_health}")
        print(f"Enemy health: {enemy_health}")
        
    def dungeon_menu(self):
        [print(f"{num+1}: {value}") for num, value in enumerate(script.room_menu["options"])]

    def kitchen_menu(self):
    [print(f"{num+1}: {value}") for num, value in enumerate(script.room_menu["options"])]

    def hall_menu(self):
    [print(f"{num+1}: {value}") for num, value in enumerate(script.room_menu["options"])]

    def toilet_menu(self):
    [print(f"{num+1}: {value}") for num, value in enumerate(script.room_menu["options"])]

    def bedroom_menu(self):
    [print(f"{num+1}: {value}") for num, value in enumerate(script.room_menu["options"])]

    def exit_screen(self):
        print(script.exit_screen['message'])


