
from encounter import Encounter
from game import Game
import tkinter as tk

class Main(tk.Tk):
    def __init__(self, encounter_text=None):
        super().__init__()

        self.encounter_text = []

        self.title("Seven Seats")
        self.geometry("640x640")

        initial_instructions = tk.Label(self, text="This is where the backstory will show.", bg="lightgrey", fg="black", pady=10)

        self.encounter_text.append(initial_instructions)

        for text in self.encounter_text:
            text.pack(side=tk.TOP, fill=tk.X)

        self.text_create = tk.Text(self, height=3, bg="white", fg="black")
        self.text_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_create.focus_set()

        self.bind("<Return>", self.next())

        self.game_canvas= tk.Canvas(self)       # background canvas for the game

        self.story_frame = tk.Frame(self.game_canvas)

        self.scrollbar = tk.Scrollbar(self.game_canvas, orient="vertical", command=self.game_canvas.yview)

        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

    def next(self):
        for text in self.encounter_text:
            text_index = self.encounter_text.index(text)
            text_index += 1

    def add_text(self):
        

    def remove_text(self):
        text = event.widget
        self.encounter_text.remove(event.widget)
        event.widget.destroy()

        if __name__ == '__main__':
            game = Main()
            game.mainloop()
