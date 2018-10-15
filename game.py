import time

from character import Character
from encounter import *
from item import Item

"""main class"""

class Game:
    def __init__(self):
        pass

    def play(self):
        encounter = Encounter()

        encounter.intro_room()


    def choice(self, choice_text, choice_input, option_1, option_2):
        """ this method will hold code that tracks when the player has made a choice """
        choosing = True
        while choosing:
            print(choice_text, "\n")
            # let the reader see the story for a bit before moving on
            # may have to use root.after() instead when implementing tKinter
            try:
                time.sleep(10)
            except KeyboardInterrupt:
                # allow player to type ctrl + C to skip reading time
                # may want to try and change this later so it works with any keyboard input
                print(" ")
            print("-------------- \n ")
            choice = input(choice_input + "\n: ")
            if choice.lower() == 'a':
                option_1
                choosing = False
            elif choice.lower() == 'b':
                option_2
                choosing = False
            else:
                pass

if __name__ == "__main__":
    game = Game()
    game.play()
