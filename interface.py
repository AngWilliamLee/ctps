from typing import TypeVar

import script

C = TypeVar("C")


def prompt_choice(message: str, options: list[C], prompt: str) -> C:
    """Helper function to prompt the user for a choice."""
    print(message)
    for i, value in enumerate(options, start=1):
        print(f"{i}: {value}")
    choice = int(input(prompt))
    return options[choice - 1]


class Interface:

    def prompt(self):
        return script.prompt

    def start_menu(self):
        return prompt_choice(script.start_menu['title'], script.start_menu["options"], script.prompt)

    def combat_menu(self, player_health, enemy_health):
        print(f"Your health: {player_health}")
        print(f"Enemy health: {enemy_health}")

    def dungeon_menu(self):
        return prompt_choice(script.dungeon_menu['message'], script.dungeon_menu["options"], script.prompt)

    def kitchen_menu(self):
        return prompt_choice(script.kitchen_menu['message'], script.kitchen_menu["options"], script.prompt)

    def hall_menu(self):
        return prompt_choice(script.hall_menu['message'], script.hall_menu["options"], script.prompt)

    def toilet_menu(self):
        return prompt_choice(script.toilet_menu['message'], script.toilet_menu["options"], script.prompt)

    def bedroom_menu(self):
        return prompt_choice(script.bedroom_menu['message'], script.bedroom_menu["options"], script.prompt)

    def exit_screen(self):
        print(script.exit_screen['message'])

    def death_msg(self):
        print(script.death_msg)

    def win_msg(self):
        print(script.win_msg)

    def caught_msg(self):
        print(script.caught_msg)


# m = Interface()
# m.kitchen_menu()


def prompt():
    return script.prompt


def start_menu():
    print(script.start_menu['title'])
    [
        print(f"{num+1}: {value}")
        for num, value in enumerate(script.start_menu["options"])
    ]
    choice = int(input(script.prompt))
    return script.start_menu['options'][choice - 1]


def combat_menu(player_health, enemy_health):
    print(f"Your health: {player_health}")
    print(f"Enemy health: {enemy_health}")


def dungeon_menu():
    print(script.dungeon_menu['message'])
    [
        print(f"{num+1}: {value}")
        for num, value in enumerate(script.dungeon_menu["options"])
    ]
    choice = int(input(script.prompt))
    return script.dungeon_menu['options'][choice - 1]


def kitchen_menu():
    print(script.kitchen_menu['message'])
    [
        print(f"{num+1}: {value}")
        for num, value in enumerate(script.kitchen_menu["options"])
    ]
    choice = int(input(script.prompt))
    return script.kitchen_menu['options'][choice - 1]


def hall_menu():
    print(script.hall_menu['message'])
    [
        print(f"{num+1}: {value}")
        for num, value in enumerate(script.hall_menu["options"])
    ]
    choice = int(input(script.prompt))
    return script.hall_menu['options'][choice - 1]


def toilet_menu():
    print(script.toilet_menu['message'])
    [
        print(f"{num+1}: {value}")
        for num, value in enumerate(script.toilet_menu["options"])
    ]
    choice = int(input(script.prompt))
    return script.toilet_menu['options'][choice - 1]


def bedroom_menu():
    print(script.bedroom_menu['message'])
    [
        print(f"{num+1}: {value}")
        for num, value in enumerate(script.bedroom_menu["options"])
    ]
    choice = int(input(script.prompt))
    return script.bedroom_menu['options'][choice - 1]


def exit_screen():
    print(script.exit_screen['message'])


def death_msg():
    print(script.death_msg)


def win_msg():
    print(script.win_msg)


def caught_msg():
    print(script.caught_msg)
