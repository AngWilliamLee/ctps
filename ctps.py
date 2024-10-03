import data
import interface
import battle


class Game:

    def __init__(self):
        self.interface = interface.Interface()
        self.player = None
        self.princess = None
        self.rooms = []
        self.now = 0

    def setup(self):
        self.player = data.createPlayer()
        self.rooms = data.createRooms()
        self.princess = self.rooms[-1].get_enemies()[-1]
        if self.interface.prompt_menu('start') == 'exit':
            self.interface.exit_screen()
            exit()

    def isover(self):
        if self.player.isdead():
            self.interface.death_msg()
            return True
        elif self.princess.isdead():
            if all([room.all_enemies_defeated() for room in self.rooms]):
                self.interface.win_msg()
            else:
                self.interface.caught_msg()
            return True
        return False

    def next_room(self):
        if self.now < len(self.rooms) - 1:
            self.now += 1

    def prev_room(self):
        if self.now > 0:
            self.now -= 1

    def get_now_room(self):
        return self.rooms[self.now]

    def get_now_room_name(self):
        return self.rooms[self.now].get_name()

    def get_next_room_name(self):
        if self.now < len(self.rooms) - 1:
            return self.rooms[self.now + 1].get_name()
        else:
            return "WALL"

    def get_prev_room_name(self):
        if self.now - 1 >= 0:
            return self.rooms[self.now - 1].get_name()
        else:
            return "WALL"

    def get_choice(self):
        "Dispalys and gets player choice. Display results afterwards"
        room_name = self.get_now_room_name().lower()
        choice = self.interface.prompt_menu(room_name)
        print(choice + '\n')
        if choice == 'Move to next room':
            self.next_room()
        elif choice == 'Move to previous room':
            self.prev_room()
        elif choice == 'Look around':

            combat = battle.Battle(self.player, self.get_now_room())
            combat.battle_start()

        else:
            print("Invalid choice")
        print()
