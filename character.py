class Character:

    def __init__(self, health, damage=0):
        self.health = health
        self.damage = damage

    def attack(self, character):
        """
        Deal damage to another character object
        """
        character.receive_damage(self.damage)
        # print("Die")

    def receive_damage(self, damage: int) -> None:
        """
        Remove health
        """
        self.health -= damage
        # print("Ouch")

    def isdead(self) -> bool:
        """
        Returns status of character (dead or alive)
        """
        return self.health <= 0

    def get_health(self) -> int:
        return self.health

    def get_type(self) -> str:
        raise NotImplementedError


class Player(Character):
    def get_type(self) -> str:
        return "Player"


class Soldier(Character):
    def get_type(self) -> str:
        return "Soldier"


class Princess(Character):
    def get_type(self) -> str:
        return "Princess"
