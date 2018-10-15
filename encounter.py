# import time
from game import Game

"""class for creating each encounter within the game"""

class Encounter:
    def __init__(self):
        # self.name = name
        pass

    # def test(self):
    #     print("Still figuring out how this works.")

    # def encounter_text(self, text):
    #     print(text)

    def intro_room(self):
        game = Game()
        # intro_room = Encounter()
        # bother_omar = Encounter()
        # leave_omar_alone = Encounter()
        print("It's early. \n \nYou can tell that its morning from the sound of birds outside your window, but even behind your closed eyelids, you know the sun hasn't yet peaked from beyond the horizon. \n \nYou let your eyelids part and turn your head slightly towards the door. \nYour brother, Omar is sitting across the room, perched against the window.\nHis face is dark and brooding this morning.")
        game.choice("", "a) You could walk over to him and ask what he's planning, or b) allow the stillness to persist for a few more moments.", "this", "that")

    def bother_omar(self):
        # bother_omar = Encounter()
        print("\nYou push yourself off the couch and almost silently slip across the room. \n \nNot silently enough. Omar turns his head to the side and looks at you out of the side of his eye. ")

    def leave_omar_alone(self):
        # leave_omar_alone = Encounter()
        print("\nOther things...")
