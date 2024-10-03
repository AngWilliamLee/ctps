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

    def attack(self, attacker, defender):
        defender.receive_damage(attacker.damage)
        if isinstance(attacker, character.Player):
            print(
                f"You attacked the {defender.get_type()}! {defender.get_type()} health: {defender.get_health()}"
            )
        else:
            print(
                f"{attacker.get_type()} attacked you! Your health: {defender.get_health()}"
            )

    # def player_attack(self):
    #     source = self.player
    #     target = self.room.get_enemies()[0]
    #     source.attack(target)
    #     print(
    #         f"You attacked the {target.get_type()}! {target.get_type()} health: {target.get_health()}"
    #     )
    #     if target.isdead():
    #         if target.get_type() == "Princess":
    #             print("Princess is now unconcious! Time to escape!")
    #         else:
    #             print("Soldier defeated!")
    #         self.room.remove_enemy()
    #     if self.room.all_enemies_defeated():
    #         print("All soldiers in the room are defeated!")

    # def enemy_attack(self):
    #     source = self.room.get_enemies()[0]
    #     target = self.player
    #     source.attack(target)
    #     print(
    #         f"{source.get_type()} attacked you! Your health: {target.get_health()}"
    #     )

    def battle_over(self):
        return self.player.isdead() or self.room.all_enemies_defeated()
