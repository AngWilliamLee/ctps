import data, interface

class Game:
    def __init__(self):
        self.interface = None
        self.player = None
        self.princess = None
        self.rooms = []
        self.now = 0
        

    def setup(self):
        self.interface = interface.Interface()
        self.player = data.createPlayer()
        self.princess = data.createPrincess()
        self.rooms = data.createRooms()
        self.interface.start_menu()

    def isover(self):
        return self.player.isdead() or self.princess.isdead()

    def next_room(self):
        if self.now < len(self.rooms) - 1:
            self.now += 1
            
    def prev_room(self):
        if self.now > 0:
            self.now -= 1
    
    def get_now_room(self):
        return self.rooms[self.now]
        
    def get_next_room(self):
        if self.now < len(self.rooms) - 1:
            return self.rooms[self.now + 1].get_name()
        else:
            return "WALL"
    
    def get_prev_room(self):
        if self.now - 1 >= 0:
            return self.rooms[self.now - 1].get_name()
        else:
            return "WALL"

    
    def get_choice(self):
        now_room = self.get_now_room()
        choices = ["Look around"]
        if now_room != "Bedroom":
            choices.append(f"Next room: {self.get_next_room()}")
        if now_room != "Dungeon":
            choices.append(f"Previous room: {self.get_prev_room()}")

        print(f"You are in {self.get_now_room()}")
        print("-choices-")
        for num, choice in enumerate(choices):
            print(f"{num+1}. {choice}")



    def get_choice(self):
        "Dispalys and gets player choice. Display results afterwards"
        choice = input("Enter choice: ")
        if choice == '1':
            self.next_room()
        elif choice == '2':
            self.prev_room()
        elif choice == '3':
            print("LOOKING AROUND")
        else:
            print("Invalid choice")

