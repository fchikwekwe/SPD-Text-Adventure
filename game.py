import time

from character import Character
from encounter import *
from item import Item

"""main class"""

class Game:
    def __init__(self):
        self.bother_omar =

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

    def bother_omar(self):
        print("\nYou push yourself off the couch and almost silently slip across the room. \n \nNot silently enough. Omar turns his head to the side and looks at you out of the side of his eye. ")

    def leave_omar_alone(self):
        print("\nOther things...")

    def play(self):
        # intro text shows; instructions show
        self.intro()
        self.time_lapse()
        # first room text shows
        print("It's early. \n \nYou can tell that its morning from the sound of birds outside your window, but even behind your closed eyelids, you know the sun hasn't yet peaked from beyond the horizon. \n \nYou let your eyelids part and turn your head slightly towards the door. \nYour brother, Omar is sitting across the room, perched against the window.\nHis face is dark and brooding this morning.")
        # allow time for user to read text
        self.time_lapse()
        choosing = True
        while choosing:
            intro_room = input("a) You could walk over to him and ask what he's planning, or b) allow the stillness to persist for a few more moments.")
            if intro_room.lower() == "a":
                self.bother_omar
            elif intro_room.lower() == "b":
                self.leave_omar_alone
            else:
                pass



if __name__ == "__main__":
    game = Game()
    game.play()
