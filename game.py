from termcolor import colored
from os import system, name
import tkinter as tk

from main import Main
from character import Character
from encounter import Encounter
# from item import Item

"""main class"""

class Game(tk.Tk):
    def __init__(self, choices=None):
        self.choices = []
        # self.bind("<Return>"

    def add_choice(self, encounter_name):
        """this method will add player choices to the self.choices list so that they can see them at the end of the game"""
        print(encounter_name)
        self.choices.append(encounter_name)

    def intro(self):
        """this is where the game instructions will show and backstory"""
        print("This is where the backstory will show.")
        print("This is where instructions for the user will show.")

    # I feel that simple user input is superior to using time lapse because it gives the user more control
    # I may come back to time lapse later if I want to give the game control in some areas

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

    def test(self):
        # first room of the game; waking up
        test = Main()
        self.add_choice("test")
        self.clear()
        test.encounter_text.append("It's early. \n \nYou can tell that its morning from the sound of birds outside your window, but even behind your closed eyelids, you know the sun hasn't yet peaked from beyond the horizon. \n \nYou let your eyelids part and turn your head slightly towards the door. \nYour brother, Omar is sitting across the room, perched against the window.\nHis face is dark and brooding this morning.")
        print(test.encounter_text)
        # intro_room.encounter_text.append(False)
        # intro_room.print_encounter_text()
        # self.clear()
        # self.choice("a) You could walk over to him and ask what he's planning, or b) allow the stillness to persist for a few more moments.", self.bother_omar, self.leave_omar_alone)

    def intro_room(self):
        # first room of the game; waking up
        intro_room = Encounter("intro room")
        self.add_choice(intro_room)
        self.clear()
        intro_room.encounter_text.append("It's early. \n \nYou can tell that its morning from the sound of birds outside your window, but even behind your closed eyelids, you know the sun hasn't yet peaked from beyond the horizon. \n \nYou let your eyelids part and turn your head slightly towards the door. \nYour brother, Omar is sitting across the room, perched against the window.\nHis face is dark and brooding this morning.")
        intro_room.encounter_text.append(False)
        intro_room.print_encounter_text()
        self.clear()
        self.choice("a) You could walk over to him and ask what he's planning, or b) allow the stillness to persist for a few more moments.", self.bother_omar, self.leave_omar_alone)

    def bother_omar(self):
        # you decide to walk over to Omar
        bother_omar = Encounter("bother omar")
        self.clear()
        bother_omar.encounter_text.append("\nYou push yourself off the couch and almost silently slip across the room. \n \nNot silently enough. Omar turns his head to the side and looks at you out of the side of his eye. \n \n'Good morning, brother. Did you sleep at all?' \nHe grunts softly and shakes his head. 'I'm surprised that you three were able to.' \nYou look back at the main room and see your sisters asleep on the other sofa across from where you just were.\n")
        bother_omar.encounter_text.append(False)
        bother_omar.print_encounter_text()
        self.clear()
        self.choice("a) Make a joking comment b) Scold your brother for staying awake all night again", self.joke_with_omar, self.scold_omar)

    def leave_omar_alone(self):
        # you enjoy the silence and observe your brother for a bit
        leave_omar_alone = Encounter("leave omar alone")
        self.clear()
        leave_omar_alone.encounter_text.append("\nA soft blast echoes in the distance and you see a shiver go through Omar's body. \nHe acts tough when others are watching, but deep down you still see your unsure little brother in there. \n \nA calm wave passes over the room before another blast makes him stand and turn around. \nHe sees that you're awake and nods in your direction. \n \n'Omar, did you sleep at all?', you ask almost under your breath.\n \nHe shakes his head as he crosses towards the kitchen. \n \n'How could you three sleep with all the bombs last night?'\nYou turn your head the other direction to look at your little sisters who are sleeping on the couch across from yours.\n")
        leave_omar_alone.encounter_text.append(False)
        leave_omar_alone.print_encounter_text()
        self.clear()
        self.choice("a) Make a joking comment b) Scold your brother for staying awake all night again", self.joke_with_omar, self.scold_omar)

    def joke_with_omar(self):
        # you try to make things light; Omar smiles
        joke_with_omar = Encounter("joke with omar")
        self.clear()
        joke_with_omar.encounter_text.append("\n'You know, you could probably bang a pot right next to their heads, and they'd still sleep until the sun came up.'\n \nYou see his guard loosen a bit as he lets out a quiet scoff, smiling slightly.\n'I don't think they'd appreciate it if we tested that out,' he says turning to the kitchen to grab his bag.\n \n'Don't leave yet,' you say, 'Let's wait at least until this round have moved on.'\nAnother distant blast sounds, followed by one that sounds a little closer. \n'We still have the same needs. Whether they're here or not.'\nHe's cold again. Distancing himself from you.\n\nYou respond, 'We have enough food for two more days, let's wait a few hours and see.'\n")
        joke_with_omar.encounter_text.append(False)
        joke_with_omar.print_encounter_text()
        self.clear()
        self.choice("A loud persistent knock on the door interrupts your conversation.\nYou hear Alia sit-up. Raya rolls over and lets out a little moan. \na) Let them knock for a bit longer b) Go over to the door and find out who it is.", self.let_them_knock, self.check_whos_there)

    def scold_omar(self):
        # your frustration spills over a bit; Omar recedes from you
        scold_omar = Encounter("scold omar")
        self.clear()
        scold_omar.encounter_text.append("\nYour brow furrows as you lean forward.\n'Omar, it's so hard to look after you when your refuse to listen to me.'\n \nRegret washes over you as the words leave your lips. Your brother tenses as he rises and stalks across the room.\n'Then don't worry about me,' he quips, 'we might all be dead soon anyway.'\n \nHis boxy frame is imposing as he pulls his backpack over his left shoulder.\n'Brother, how can I let you leave without worrying?,' glancing at your sisters, you continue, 'The three of you are all that I have.'\n")
        scold_omar.encounter_text.append(False)
        scold_omar.print_encounter_text()
        self.clear()
        self.choice("A loud persistent knock on the door interrupts your conversation.\nYou hear Alia sit-up. Raya rolls over and lets out a little moan. \na) Let them knock for a bit longer b) Go over to the door and find out who it is.", self.let_them_knock, self.check_whos_there)

    def let_them_knock(self):
        # someone is knocking; maybe they'll go away
        let_them_knock = Encounter("let them knock")
        self.clear()
        let_them_knock.encounter_text.append("\nThe knock rings louder the second time around. You look at Omar and hold your hand up towards him as if to tell him not to move yet.\n \n'I come in peace!' a voice calls out from beyond the door. 'And I have your last paycheck.' You would recognize Than's voice anywhere.\nOmar is a few feet behind you as you take steps toward the door. He signals for you to use the peephole to confirm Than's identity.\n You lean towards the closed door and look through the small bit of glass. Outside you see a short, stocky man with dark hair and ruddy cheeks. It's your boss at the transportation agency.\nYour hand reaches for the deadbolt lock and you open the door slowly, allowing Than to come in.\n\nAlia is standing in front on the couch now, arms crossed in her defiant, eleven-year-old way. Even Raya is sitting up looking at the man who has come in to your house.\n")
        let_them_knock.encounter_text.append(False)
        let_them_knock.encounter_text.append("'You could've gotten me killed making me stand outside like that!' Than sighs, the redness in his face spreading from adrenaline. \n'I've never known you to be so rude to a visitor before.' He's referencing your desk work at the transportation agency.\nYou sigh. 'Can't be too careful these days. I'm sorry for putting you at risk, Than.'\n'Yes, I know,' he responds. 'Your heart is too big for that. Which brings me to the reason for my visit.\n\n'I can't stay long. But you've been good to me, good to the agency.")
        let_them_knock.encounter_text.append("\nAs a final goodbye, I have a van waiting for you outside. It has supplies that need to be delievered...' \nYou interrupt, 'Than, this doesn't sound like a goodbye present.' \n'Let me finish,' he continues. 'The supplies need to be delivered to a hospital in the next town over. In the much safer town that still has a working hospital. There is space in this van.' he steps toward you and leans forward, 'take your family and be safe before its too late.'")
        let_them_knock.encounter_text.append(False)
        let_them_knock.print_encounter_text()
        self.clear()
        self.choice("'Than.' you sigh, 'Thank you for this.' a) ask about the supplies b) ask about the amount of space that there is in the vehicle", self.check_supplies, self.check_space)

    def check_whos_there(self):
        # you go to the door
        check_whos_there = Encounter("check whos there")
        self.clear()
        check_whos_there.encounter_text.append("\nYou walk over to the door and ask in a calm voice, 'who is it?'\nAlia is standing in front on the couch now, arms crossed in her defiant, eleven-year-old way. \nA voice from the other side of the door responds, 'Its your lifeline. I have good news for you, if you'll let me in.'\n\nYou would recognize Than's voice anywhere. Omar is a few feet behind you as you take steps toward the door. He signals for you to use the peephole to confirm Than's identity.\nYou lean towards the closed door and look through the small bit of glass. Outside you see a short, stocky man with dark hair and ruddy cheeks. It's your boss at the transportation agency.\nYour hand reaches for the deadbolt lock and you open the door slowly, allowing Than to come in.\n\nNow, even Raya is sitting up looking at the man who has come in to your house.\n")
        check_whos_there.encounter_text.append(False)
        check_whos_there.encounter_text.append("\n'Young one, its good to see you again!' he exclaims.\n'It's so dangerous for you to be outside like that, Than.'\n'Yes, I know,' he responds. 'But I had to come here with news for you. Which brings me to the reason for my visit.\n\n'I can't stay long. But you've been good to me, good to the agency. \nAs a final goodbye, I have a van waiting for you outside. It has supplies that need to be delievered...' \nYou interrupt, 'Than, this doesn't sound like a goodbye present.' \n'Let me finish,' he continues. 'The supplies need to be delivered to a hospital in the next town over. In the much safer town that still has a working hospital. There is space in this van.' he steps toward you and leans forward, 'take your family and be safe before its too late.'")
        check_whos_there.encounter_text.append(False)
        check_whos_there.print_encounter_text()
        self.clear()
        self.choice("'Than.' you sigh, 'Thank you for this.' a) ask about the supplies b) ask about the amount of space that there is in the vehicle", self.check_supplies, self.check_space)

    def check_supplies(self):
        # you ask first about the supplies that you must carry
        check_supplies = Encounter("check supplies")
        self.clear()
        check_supplies.encounter_text.append("\n'What are the supplies that I'm taking?' you say jumping right into the job details.\n'You were always a hard worker,' Than says smirking. He explains that you have a few gurneys and a lot of surgical supples that have to be taken.\n'Overall,' he continues, 'It should leave space enough for seven people if you really are pushing it. But definitely enough space for the people that I see here.'\nThan comes close to you and gives you a hug. A tear comes to his eye as he explains that this might be the last time that you see one another again.")
        check_supplies.encounter_text.append("\n\nIf he can make it out alive, the company that owns the transportation agency he was managing has paid for a ticket out of the country for him.\nThis is his way of paying it forward to you. As he leaves your small home, you can tell that the air raid from last night seems to be subsiding. The crack of dawn marks the new day for you.\n\n'Seven seats...' you think 'Maybe there are others who need a way out of here as well.\n'")
        check_supplies.print_encounter_text()
        input(colored("End of Chapter One. Thanks for playing.", "cyan", attrs=["bold"]))
        sys.exit()


    def check_space(self):
        # you ask first about the amount of space for people
        check_space = Encounter("check space")
        self.clear()
        check_space.encounter_text.append("\n'How many of us can fit in the vehicle?' you ask, 'I have three siblings.' \nThan waives your question away. 'There are seven seats in the van. Even with the supplies that are there, you'll be fine on space for your four. In fact, you can take some others as well if you'd like.' \nThan comes close to you and gives you a hug. A tear comes to his eye as he explains that this might be the last time that you see one another again.\n\nIf he can make it out alive, the company that owns the transportation agency he was managing has paid for a ticket out of the country for him.\nThis is his way of paying it forward to you. As he leaves your small home, you can tell that the air raid from last night seems to be subsiding. The crack of dawn marks the new day for you.\n\n'Seven seats...' you think 'Maybe there are others who need a way out of here as well.\n'")
        check_space.print_encounter_text()
        input(colored("End of Chapter One. Thanks for playing.", "cyan", attrs=["bold"]))
        exit()


if __name__ == "__main__":

    # time to play
    game = Game()
    game.play()
    main = Main()
    main.mainloop()
