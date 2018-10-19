
from encounter import Encounter
from game import Game
import tkinter as tk

class Main(tk.Tk):
    def __init__(self, encounter_text=None, instructions=None):
        super().__init__()

        if not encounter_text:
            self.encounter_text = []
        else:
            self.encounter_text = encounter_text

        if not instructions:
            self.instructions = []
        else:
            self.instructions = instructions

        self.game_canvas= tk.Canvas(self)       # background canvas for the game

        self.story_frame = tk.Frame(self.game_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.game_canvas, orient="vertical", command=self.game_canvas.yview)

        self.game_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.title("Seven Seats")
        self.geometry("640x640")

        self.text_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        self.game_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.game_canvas.create_window((0,0), window=self.story_frame, anchor="n")

        self.text_create = tk.Text(self, height=3, bg="white", fg="black")
        self.story_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_create.focus_set()

        instructions = tk.Label(self, text="This is where the instructions will show.", bg="lightgrey", fg="black", pady=10)
        instructions.bind("<Button-1>", self.remove_text)

        self.instructions.append(instructions)

        self.bind("<Return>", self.next)

        for text in self.instructions:
            text.pack(side=tk.BOTTOM, fill=tk.X)

        for text in self.encounter_text:
            text.pack(side=tk.TOP, fill=tk.X)

        self.bind("<Return>", self.add_text)

    def next(self):
        for text in self.encounter_text:
            text_index = self.encounter_text.index(text)
            text_index += 1

    def add_text(self, event=None):
        for text in Encounter.encounter_text:
            self.encounter_text.append(text)

    def remove_text(self):
        text = event.widget
        self.encounter_text.remove(event.widget)
        event.widget.destroy()

    def task_width(self, event):
        canvas_width = event.width
        self.game_canvas.itemconfig(self.canvas_frame, width = canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.game_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1
            self.game_canvas.yview_scroll(move, "units")


if __name__ == '__main__':
    game = Main()
    game.mainloop()
