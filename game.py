import time

from character import Character
from encounter import *
from item import Item

"""main class"""

class Game:
    def __init__(self):
        self.choices = []

    def add.choice(self):
        

    def intro(self):
        """this is where the game instructions will show and backstory"""
        print("This is where the backstory will show.")
        print("This is where instructions for the user will show.")

    def time_lapse(self):
        # let the reader see the story for a bit before moving on
        # may have to use root.after() instead when implementing tKinter
        try:
            time.sleep(10)
        except KeyboardInterrupt:
            # allow player to type ctrl + C to skip reading time
            # may want to try and change this later so it works with any keyboard input
            print(" ")

    def play(self):
        # declare objects
        intro_room = Intro_Room()
        bother_omar = Bother_Omar()
        leave_omar_alone = Leave_Omar_Alone()

        # intro text shows; instructions show
        self.intro()
        self.time_lapse()
        self.intro_room()

    def intro_room(self):
        # first room text showss
        intro_room.encounter_text()
        # allow time for user to read text
        self.time_lapse()
        intro_room.choice("a) You could walk over to him and ask what he's planning, or b) allow the stillness to persist for a few more moments.", bother_omar.encounter_text, leave_omar_alone.encounter_text)

    def bother_omar(self):
        # allow time for user to read text
        self.time_lapse()
        bother_omar.choice("", option_1, option_2)



if __name__ == "__main__":
    game = Game()
    game.play()
