import ctps
import interface

if __name__ == "__main__":
    game = ctps.Game()
    game.setup()
    if interface.prompt_menu('start') == 'exit':
        interface.exit_screen()
        exit()

    while not game.isover():
        choice = game.get_choice()
        game.do_choice(choice)
    game.end_game()
