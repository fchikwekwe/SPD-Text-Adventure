# import time

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
        print("\nYou push yourself off the couch and almost silently slip across the room. \n \nNot silently enough. Omar turns his head to the side and looks at you out of the side of his eye. \n \n'Good morning, brother. Did you sleep at all?' \nHe grunts softly and shakes his head. 'I'm surprised that you three were able to.' \nYou look back at the main room and see your sisters asleep on the other sofa across from where you just were.\n")

class Leave_Omar_Alone(Encounter):
    def encounter_text(self):
        print("\nA soft blast echoes in the distance and you see a shiver go through Omar's body. \nHe acts tough when others are watching, but deep down you still see your unsure little brother in there. \n \nA calm wave passes over the room before another blast makes him stand and turn around. \nHe sees that you're awake and nods in your direction. \n \n'Omar, did you sleep at all?' \n \nHe shakes his head as he crosses towards the kitchen. \n \n'How could you three sleep with all the bombs last night?'\nYou turn your head the other direction to look at your little sisters who are sleeping on the couch across from yours.\n")

class Joke_With_Omar(Encounter):
    def encounter_text(self):
        print("\n'You know, you could probably bang a pot right next to their heads, and they'd still sleep until the sun came up.'\n \nYou see his guard loosen a bit as he lets out a quiet scoff and smiles slightly.\n'I don't think they'd appreciate it if we tested that out,' he says turning to the kitchen to grab his bag.\n \n'Don't leave yet,' you say, 'Let's wait at least until this round have moved on'\n Another distant blast sounds, followed by one that sounds a little closer. \n'We still have the same needs. Whether they're here or not.'\nHe's cold again. Distancing himself from you.\n'We still have enough food for two more days, let's wait a few hours and see'\n")

class Scold_Omar(Encounter):
    def encounter_text(self):
        print("\nYour brow furrows as you lean forward.\n'Omar, it's so hard to look after you when your refuse to listen to me.'\n \nRegret washes over you as the words leave your lips. Your brother tenses as he rises and stalks across the room.\n'Then don't worry about me,' he quips, 'we might all be dead soon anyway.'\n \nHis boxy frame is imposing as he pulls his backpack over his left shoulder.\n'Brother, how can I let you leave without worrying?,' glancing at your sisters, you continue, 'The three of you are all that I have.'\n")
