import ctps

if __name__ == "__main__":
    game = ctps.Game()
    game.setup()

    while not game.isover():
        choice = game.get_choice()
        game.do_choice(choice)
    game.end_game()
