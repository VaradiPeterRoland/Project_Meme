import sys
import Meme_UI
from virus import meme_virus
from best_game import best_game
from ninegag import get_fresh_meme
from random_meme_sound import get_random_meme_sound
from hymn import meme_hymn


def choose():
    inputs = Meme_UI.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        best_game()
    elif option == "2":
        get_fresh_meme()
    elif option == "3":
        meme_hymn()
    elif option == "4":
        get_random_meme_sound()
    elif option == "5":
        meme_virus(10)
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Best Game Ever",
               "9gag Dank Memes",
               "Meme Hymn",
               "Random Meme Sound For Random Fun",
               "Virus"]

    Meme_UI.print_menu("Meme Menu", options, "Exit Program")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except:
            raise KeyError("There is no such option.")


if __name__ == '__main__':
    main()
