import time

from character import Character
from encounter import *
from item import Item

"""main class"""

class Game:
    def __init__(self):
        """eventually this list will store player choices and show them to the player at the end of the game"""
        self.choices = []

    def add_choice(self):
        """this method will add player choices to the self.choices list so that they can see them at the end of the game"""

    def intro(self):
        """this is where the game instructions will show and backstory"""
        print("This is where the backstory will show.")
        print("This is where instructions for the user will show.")

    # I feel that simple user input is superior to using time lapse because it gives the user more control
    # I may come back to this later if I want to give the game control in some areas

    # def time_lapse(self):
    #     # let the reader see the story for a bit before moving on
    #     # may have to use root.after() instead when implementing tKinter
    #     try:
    #         time.sleep(10)
    #     except KeyboardInterrupt:
    #         # allow player to type ctrl + C to skip reading time
    #         # may want to try and change this later so it works with any keyboard input
    #         print(" ")

    def play(self):
        # intro text shows; instructions show
        self.intro()
        input("Press enter to continue...")
        # start the game
        self.intro_room()


    def intro_room(self):
        # first room text showss
        intro_room.encounter_text()
        # allow time for user to read text
        input("Press enter to continue...")
        intro_room.choice("a) You could walk over to him and ask what he's planning, or b) allow the stillness to persist for a few more moments.", self.bother_omar, self.leave_omar_alone)

    def bother_omar(self):
        bother_omar.encounter_text()
        # allow time for user to read text
        input("Press enter to continue...")
        bother_omar.choice("a) Make a joking comment b) Scold your brother for staying awake all night again", self.joke_with_omar, self.scold_omar)

    def leave_omar_alone(self):
        pass


if __name__ == "__main__":
    # instatiate objects
    intro_room = Intro_Room()
    bother_omar = Bother_Omar()
    leave_omar_alone = Leave_Omar_Alone()

    game = Game()
    game.play()
