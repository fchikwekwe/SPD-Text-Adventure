
from game import Game

"""choice attributes"""

class Choice:
    def __init__(self, name, choice_description):
        self.name = name
        self.choice_description = choice_description

    def show_choices(self, name, description):
        for choice in game.choices:
            print(choice)
