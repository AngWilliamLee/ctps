from typing import TypeVar

import script

C = TypeVar("C")


def prompt_choice(message: str, options: list[str], prompt: str) -> str:
    """Helper function to prompt the user for a choice."""
    print(message)
    for i, value in enumerate(options, start=1):
        print(f"{i}: {value}")
    choice = int(input(prompt))
    return options[choice - 1]


class Interface:

    def prompt(self):
        return script.prompt

    def combat_menu(self, player_health, enemy_health):
        print(f"Your health: {player_health}")
        print(f"Enemy health: {enemy_health}")

    def prompt_menu(self, room_name: str) -> str:
        return prompt_choice(script.menu[room_name]['message'], script.menu[room_name]["options"], script.prompt)

    def exit_screen(self):
        print(script.exit_screen['message'])

    def death_msg(self):
        print(script.death_msg)

    def win_msg(self):
        print(script.win_msg)

    def caught_msg(self):
        print(script.caught_msg)
