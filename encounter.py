import time


"""class for creating each encounter within the game"""

class Encounter:
    def __init__(self):
        # self.name = name
        pass

    def encounter_text(self):
        raise notImplementedError()

    def choice(self, choice_input, option_1, option_2):
        """ this method will hold code that tracks when the player has made a choice """
        choosing = True
        while choosing:
            print("-------------- \n ")
            choice = input(choice_input + "\nPlease Type 'a' or 'b': ")
            if choice.lower() == 'a':
                option_1()
                choosing = False
            elif choice.lower() == 'b':
                option_2()
                choosing = False
            else:
                pass

class Intro_Room(Encounter):
    def encounter_text(self):
        print("It's early. \n \nYou can tell that its morning from the sound of birds outside your window, but even behind your closed eyelids, you know the sun hasn't yet peaked from beyond the horizon. \n \nYou let your eyelids part and turn your head slightly towards the door. \nYour brother, Omar is sitting across the room, perched against the window.\nHis face is dark and brooding this morning.")

class Bother_Omar(Encounter):
    def encounter_text(self):
        print("\nYou push yourself off the couch and almost silently slip across the room. \n \nNot silently enough. Omar turns his head to the side and looks at you out of the side of his eye. \n \n 'Good morning, brother. Did you sleep at all?' \n He grunts softly and shakes his head. 'I'm surprised that you three were able to.' \n You look back at the main room and see your sisters asleep on the other sofa across from where you just were.")

class Leave_Omar_Alone(Encounter):
    def encounter_text(self):
        print("\nOther things...")

class Joke_With_Omar(Encounter):
    def encounter_text(self):
        print("\n say things")

class Scold_Omar(Encounter):
    def encounter_text(self):
        print("\n say things")
