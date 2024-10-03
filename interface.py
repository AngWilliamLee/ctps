from typing import TypeVar

import script

C = TypeVar("C")


def prompt_choice(message: str, options: list[str], prompt: str) -> str:
    """Helper function to prompt the user for a choice."""
    print(message)
    for i, value in enumerate(options, start=1):
        print(f"{i}: {value}")
    choice = input(prompt)
    while not choice.isdecimal() or int(choice) - 1 not in range(len(options)):
        print("Invalid choice.")
        choice = input(prompt)
    return options[int(choice) - 1]



def prompt():
    return script.prompt


def combat_menu(player_health, enemy_health):
    print(f"Your health: {player_health}")
    print(f"Enemy health: {enemy_health}")


def prompt_menu(room_name: str) -> str:
    return prompt_choice(script.menu[room_name]['message'], script.menu[room_name]["options"], script.prompt)


def exit_screen():
    print(script.exit_screen['message'])


def death_msg(char_type: str) -> str:
    if char_type == "Player":
        return 'You died! Try again next time'
    elif char_type == "Princess":
        return "Princess is now unconcious! Time to escape!"
    elif char_type == "Soldier":
        return "Soldier defeated!"
    raise ValueError(f"Invalid character type: {char_type!r}")


def win_msg():
    print(script.win_msg)


def caught_msg():
    print(script.caught_msg)
