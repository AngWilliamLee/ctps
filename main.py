import ctps

if __name__ == "__main__":
    game = ctps.Game()
    game.setup()

    while not game.isover():
        game.get_choice()
    game.end_game()
