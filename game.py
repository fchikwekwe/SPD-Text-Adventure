import time
from termcolor import colored
from os import system, name

from character import Character
from encounter import *
# from item import Item

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

    def clear(self):
        # this method clears the console; will use after each input
        if name == 'nt':
            _=system('cls')
        else:
            _=system('clear')

    def play(self):
        """
        Once base game is written, I need to go back here and add a game loop
        that shows player their choices so far and asks them if they would like to play again
        """
        self.clear()
        # intro text shows; instructions show
        self.intro()
        input(colored("Press enter to continue...", "cyan", attrs=["bold"]))
        self.clear()
        # start the game
        # self.intro_room()

        intro_room = Encounter()
        intro_room_function = self.encounter_room(intro_room, "It's early. \n \nYou can tell that its morning from the sound of birds outside your window, but even behind your closed eyelids, you know the sun hasn't yet peaked from beyond the horizon. \n \nYou let your eyelids part and turn your head slightly towards the door. \nYour brother, Omar is sitting across the room, perched against the window.\nHis face is dark and brooding this morning.", "a) You could walk over to him and ask what he's planning, or b) allow the stillness to persist for a few more moments.", bother_omar, self.leave_omar_alone)
        bother_omar =

        # self.encounter_room(intro_room, "a) You could walk over to him and ask what he's planning, or b) allow the stillness to persist for a few more moments.", self.bother_omar, self.leave_omar_alone)




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

    # trying to see if there is a better way to organize this code than to have seperate functions for each encounter
    # problem with this method is that I would have to call two functions within another function call
    # unfortunately, this does not simplify things; might come back to it if I think of something

    def encounter_room(self, encounter_name, encounter_story, choice_text, choice_one, choice_two):
        encounter_name = Encounter()
        encounter_name.encounter_text.append(encounter_story)
        encounter_name.encounter_text.append(False)
        encounter_name.print_encounter_text()
        self.clear()
        self.choice(choice_text, choice_one, choice_two)

    # def intro_room(self):
    #     # first room of the game; waking up
    #     intro_room = Encounter()
    #     intro_room.encounter_text.append("It's early. \n \nYou can tell that its morning from the sound of birds outside your window, but even behind your closed eyelids, you know the sun hasn't yet peaked from beyond the horizon. \n \nYou let your eyelids part and turn your head slightly towards the door. \nYour brother, Omar is sitting across the room, perched against the window.\nHis face is dark and brooding this morning.")
    #     intro_room.encounter_text.append(False)
    #     intro_room.print_encounter_text()
    #     self.choice("a) You could walk over to him and ask what he's planning, or b) allow the stillness to persist for a few more moments.", self.bother_omar, self.leave_omar_alone)

    def bother_omar(self):
        # you decide to walk over to Omar
        bother_omar = Encounter()
        bother_omar.encounter_text.append("\nYou push yourself off the couch and almost silently slip across the room. \n \nNot silently enough. Omar turns his head to the side and looks at you out of the side of his eye. \n \n'Good morning, brother. Did you sleep at all?' \nHe grunts softly and shakes his head. 'I'm surprised that you three were able to.' \nYou look back at the main room and see your sisters asleep on the other sofa across from where you just were.\n")
        bother_omar.encounter_text.append(False)
        self.clear()
        self.choice("a) Make a joking comment b) Scold your brother for staying awake all night again", self.joke_with_omar, self.scold_omar)

    def leave_omar_alone(self):
        # you enjoy the silence and observe your brother for a bit
        leave_omar_alone = Encounter()
        leave_omar_alone.encounter_text.append("\nA soft blast echoes in the distance and you see a shiver go through Omar's body. \nHe acts tough when others are watching, but deep down you still see your unsure little brother in there. \n \nA calm wave passes over the room before another blast makes him stand and turn around. \nHe sees that you're awake and nods in your direction. \n \n'Omar, did you sleep at all?', you ask almost under your breath.\n \nHe shakes his head as he crosses towards the kitchen. \n \n'How could you three sleep with all the bombs last night?'\nYou turn your head the other direction to look at your little sisters who are sleeping on the couch across from yours.\n")
        leave_omar_alone.encounter_text.append(False)
        self.clear()
        self.choice("a) Make a joking comment b) Scold your brother for staying awake all night again", self.joke_with_omar, self.scold_omar)

    def joke_with_omar(self):
        # you try to make things light; Omar smiles
        joke_with_omar = Encounter()
        joke_with_omar.encounter_text.append("\n'You know, you could probably bang a pot right next to their heads, and they'd still sleep until the sun came up.'\n \nYou see his guard loosen a bit as he lets out a quiet scoff, smiling slightly.\n'I don't think they'd appreciate it if we tested that out,' he says turning to the kitchen to grab his bag.\n \n'Don't leave yet,' you say, 'Let's wait at least until this round have moved on.'\nAnother distant blast sounds, followed by one that sounds a little closer. \n'We still have the same needs. Whether they're here or not.'\nHe's cold again. Distancing himself from you.\n\nYou respond, 'We have enough food for two more days, let's wait a few hours and see.'\n")
        joke_with_omar.encounter_text.append(False)
        self.clear()
        self.choice("A loud persistent knock on the door interrupts your conversation.\nYou hear Alia sit-up. Raya rolls over and lets out a little moan. \na) Let them knock for a bit longer b) Go over to the door and find out who it is.", self.let_them_knock, self.check_whos_there)

    def scold_omar(self):
        # your frustration spills over a bit; Omar recedes from you
        scold_omar.encounter_text()
        input(colored("Press enter to continue...", "cyan", attrs=["bold"]))
        self.clear()
        scold_omar.choice("A loud persistent knock on the door interrupts your conversation.\nYou hear Alia sit-up. Raya rolls over and lets out a little moan. \na) Let them knock for a bit longer b) Go over to the door and find out who it is.", self.let_them_knock, self.check_whos_there)

    # def let_them_knock(self):
    #     # someone is knocking; maybe they'll go away
    #     let_them_knock.encounter_text()
    #     input(colored("Press enter to continue...", "cyan", attrs=["bold"]))
    #     self.clear()
    #     let_them_knock.choice("'Than.' you sigh, 'Thank you for this.' a) ask about the supplies b) ask about the amount of space that there is in the vehicle", self.check_supplies, self.check_space)
    #
    # def check_whos_there(self):
    #     check_whos_there.encounter_text()
    #     input(colored("Press enter to continue...", "cyan", attrs=["bold"]))
    #     self.clear()
    #     check_whos_there.choice("'Than.' you sigh, 'Thank you for this.' a) ask about the supplies b) ask about the amount of space that there is in the vehicle", self.check_supplies, self.check_space)
    #
    # def check_supplies(self):
    #     check_supplies.encounter_text()
    #     input(colored("End of Chapter One. Press enter to continue...", "cyan", attrs=["bold"]))
    #     self.clear()
    #     check_supplies.choice("nothing yet", self.option_1, self.option_2)
    #
    # def check_space(self):
    #     check_space.encounter_text()
    #     input(colored("End of Chapter One. Press enter to continue...", "cyan", attrs=["bold"]))
    #     self.clear()
    #     check_space.choice("nothing yet", self.option_1, self.option_2)

if __name__ == "__main__":


    # instatiate objects
    # intro_room = Intro_Room()
    # bother_omar = Bother_Omar()
    # leave_omar_alone = Leave_Omar_Alone()
    # joke_with_omar = Joke_With_Omar()
    # scold_omar = Scold_Omar()
    # let_them_knock = Let_Them_Knock()
    # check_whos_there = Check_Whos_There()
    # check_supplies = Check_Supplies()
    # check_space = Check_Space()

    # time to play
    game = Game()
    game.play()
