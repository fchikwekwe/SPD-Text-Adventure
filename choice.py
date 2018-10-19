
from game import Game

"""Class not currently in use; future feature to be implmented later; choice attributes"""

class Choice:
    def __init__(self, name, choice_description):
        self.name = name
        self.choice_description = choice_description

    def show_choices(self, name, description):
        for choice in game.choices:
            print(choice)
