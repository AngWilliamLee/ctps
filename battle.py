import time

import character
import interface


class Battle:

    def __init__(self, player, room):
        self.player = player
        self.room = room

    def battle_start(self):
        if self.room.all_enemies_defeated():
            print("All soldiers in the room have been defeated already!")
            return
        print("YOU FOUND ENEMIES!!!!")
        while not self.battle_over():
            attacker = self.player
            defender = self.room.get_enemies()[0]
            self.attack(attacker, defender)
            if defender.isdead():
                print(interface.death_msg(defender.get_type()))
                if attacker == self.player:
                    self.room.remove_enemy()
                    defender = self.room.get_enemies()[0]
            attacker, defender = defender, attacker
            time.sleep(0.1)
        if self.room.all_enemies_defeated():
            print("All soldiers in the room are defeated!")
        print("Battle over!")

    def attack(self, attacker, defender) -> None:
        defender.receive_damage(attacker.damage)
        print(self.attack_report(attacker, defender))

    def attack_report(self, attacker, defender) -> str:
        if attacker.get_type() == "Player":
            return f"You attacked the {defender.get_type()}! {defender.get_type()} health: {defender.get_health()}"
        else:
            return f"{attacker.get_type()} attacked you! Your health: {defender.get_health()}"

    def battle_over(self):
        return self.player.isdead() or self.room.all_enemies_defeated()
