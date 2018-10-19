
from termcolor import colored

"""class for creating each encounter within the game"""

class Encounter:
    def __init__(self, name, encounter_text=None):
        # holds texts and input to display
        self.name = name
        self.encounter_text = []

    def next(self):
        input(colored("Press enter to continue...", "cyan", attrs=["bold"]))

    def print_encounter_text(self):
        # checking texts added to object list
        for text in self.encounter_text:
            # add false to list instead of print statement to get input instead
            if text == False:
                # this is the input
                self.next()
            else:
                # otherwise, print text
                text_index = self.encounter_text.index(text)
                print(self.encounter_text[text_index])
