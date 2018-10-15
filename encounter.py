import time


"""class for creating each encounter within the game"""

class Encounter:
    def __init__(self):
        # self.name = name
        pass

    # def test(self):
    #     print("Still figuring out how this works.")

    def encounter_text(self, text):
        print(text)

    def choice(self, choice_text, choice_input, option_1, option_2):
        """ this method will hold code that tracks when the player has made a choice """
        choosing = True
        while choosing:
            print(choice_text, "\n")
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
