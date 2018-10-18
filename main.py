
from encounter import Encounter
from game import Game
import tkinter as tk

class Main(tk.Tk):
    def __init__(self, encounter_text=None):
        super().__init__()

        self.encounter_text = []

        self.game_canvas= tk.Canvas(self)       # background canvas for the game
        self.story_frame = tk.Frame(self.game_canvas)

        self.scrollbar = tk.Scrollbar(self.game_canvas, orient="vertical", command=self.game_canvas.yview)

        self.game_canvas.configure(yscrolcommand=self.scrollbar.set)

        self.title("Seven Seats")
        self.geometry("640x640")

        self.text_create = tk.Text(self.story_frame, height=3, bg="white", fg="black")

        self.game_canvas.pack(side=tk.BOTTOM, fill=tk.X)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.game_canvas.create_window((0,0), window=self.story_frame, anchor="n")

        self.text_create = tk.Text(self, height=3, bg="white", fg="black")
        self.story_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_create.focus_set()

        initial_instructions = tk.Label(self, text="This is where the backstory will show.", bg="lightgrey", fg="black", pady=10)
        initial_instructions.bind("<Button-1>", self.remove_text)

        self.encounter_text.append(initial_instructions)

        self.bind("<Return>", self.next())

        for text in self.encounter_text:
            text.pack(side=tk.TOP, fill=tk.X)

    def next(self):
        for text in self.encounter_text:
            text_index = self.encounter_text.index(text)
            text_index += 1

    # def add_text(self):
    #

    def remove_text(self):
        text = event.widget
        self.encounter_text.remove(event.widget)
        event.widget.destroy()

        if __name__ == '__main__':
            game = Main()
            game.mainloop()
