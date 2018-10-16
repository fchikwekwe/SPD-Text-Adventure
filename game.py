import time
from termcolor import colored
from os import system, name

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
        self.intro_room()
        # self.encounter_room(intro_room, "a) You could walk over to him and ask what he's planning, or b) allow the stillness to persist for a few more moments.", self.bother_omar, self.leave_omar_alone)


    # trying to see if there is a better way to organize this code than to have seperate functions for each encounter
    # problem with this method is that I would have to call two functions within another function call
    # unfortunately, this does not simplify things; might come back to it if I think of something
    
    # def encounter_room(self, encounter_name, choice_text, choice_one, choice_two):
    #     encounter.encounter_text()
    #     input(colored("Press enter to continue...", "cyan", attrs=["bold"]))
    #     self.clear()
    #     encounter.choice(choice_text, choice_one, choice_two)

    def intro_room(self):
        # first room of the game; waking up
        intro_room.encounter_text()
        # using another text color so that this catches the user's eye
        input(colored("Press enter to continue...", "cyan", attrs=["bold"]))
        # clear the console after input
        self.clear()
        # first choice of the game
        intro_room.choice("a) You could walk over to him and ask what he's planning, or b) allow the stillness to persist for a few more moments.", self.bother_omar, self.leave_omar_alone)

    def bother_omar(self):
        # you decide to walk over to Omar
        bother_omar.encounter_text()
        input(colored("Press enter to continue...", "cyan", attrs=["bold"]))
        self.clear()
        bother_omar.choice("a) Make a joking comment b) Scold your brother for staying awake all night again", self.joke_with_omar, self.scold_omar)

    def leave_omar_alone(self):
        # you enjoy the silence and observe your brother for a bit
        leave_omar_alone.encounter_text()
        input(colored("Press enter to continue...", "cyan", attrs=["bold"]))
        self.clear()
        leave_omar_alone.choice("a) Make a joking comment b) Scold your brother for staying awake all night again", self.joke_with_omar, self.scold_omar)

    def joke_with_omar(self):
        # you try to make things light; Omar smiles
        joke_with_omar.encounter_text()
        input(colored("Press enter to continue...", "cyan", attrs=["bold"]))
        self.clear()
        joke_with_omar.choice("A loud persistent knock on the door interrupts your conversation.\n You hear Alia sit-up. Raya rolls over and lets out a little moan. \n", self.let_them_knock, self.check_whos_there)

    def scold_omar(self):
        # your frustration spills over a bit; Omar recedes from you
        scold_omar.encounter_text()
        input(colored("Press enter to continue...", "cyan", attrs=["bold"]))
        self.clear()
        scold_omar.choice("A loud persistent knock on the door interrupts your conversation.\nYou hear Alia sit-up. Raya rolls over and lets out a little moan. \na) Let the knock for a bit longer b) Go over to the door and find out who it is.", self.let_them_knock, self.check_whos_there)

    def let_them_knock(self):
        # someone is knocking; maybe they'll go away
        let_them_knock.encounter_text()
        input(colored("Press enter to continue...", "cyan", attrs=["bold"]))
        self.clear()
        let_them_knock.choice("", option_1, option_2)

    def check_whos_there(self):
        # I'm curious enough to try and check who it is
        pass

if __name__ == "__main__":
    # instatiate objects
    intro_room = Intro_Room()
    bother_omar = Bother_Omar()
    leave_omar_alone = Leave_Omar_Alone()
    joke_with_omar = Joke_With_Omar()
    scold_omar = Scold_Omar()

    # time to play
    game = Game()
    game.play()
