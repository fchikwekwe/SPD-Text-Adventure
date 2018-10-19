
from encounter import Encounter
# from game import Game
import tkinter as tk

""" this class deals with the GUI part of this application"""

class Main(tk.Tk):
    def __init__(self, encounter_text=None, instructions=None):
        super().__init__()
        # list for story texts
        if not encounter_text:
            self.encounter_text = ["test"]
        else:
            self.encounter_text = encounter_text
        # list for instructions / backstory
        if not instructions:
            self.instructions = []
        else:
            self.instructions = instructions

        self.game_canvas= tk.Canvas(self)       # background canvas for the game

        self.story_frame = tk.Frame(self.game_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.game_canvas, orient="vertical", command=self.game_canvas.yview)

        self.game_canvas.configure(yscrollcommand=self.scrollbar.set)
        # game title; subject to change
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

        self.instructions.append(instructions)

        # instructions are listed at the bottom of the screen
        for text in self.instructions:
            text.pack(side=tk.BOTTOM, fill=tk.X)

        for text in self.encounter_text:
            text = tk.Label(self, text=text, fg="black")
            text.pack(side=tk.BOTTOM, fill=tk.X)

        self.bind("<Return>", self.add_text)

    def next(self):
        # iterates over encounter text list
        for text in self.encounter_text:
            text_index = self.encounter_text.index(text)
            text_index += 1

    def add_text(self, event=None):
        # adds text to encounter text list so that it renders on screen
        self.encounter_text.append("It's early. \n \nYou can tell that its morning from the sound of birds outside your window, but even behind your closed eyelids, you know the sun hasn't yet peaked from beyond the horizon. \n \nYou let your eyelids part and turn your head slightly towards the door. \nYour brother, Omar is sitting across the room, perched against the window.\nHis face is dark and brooding this morning.")
        print(self.encounter_text)
        self.encounter_text.append("a) You could walk over to him and ask what he's planning, or b) allow the stillness to persist for a few more moments.")
        print(self.encounter_text)

    def remove_text(self):
        # removes last text from encounter_text list
        text = event.widget
        self.encounter_text.remove(event.widget)
        event.widget.destroy()

    def task_width(self, event):
        # regulates text width on screen
        canvas_width = event.width
        self.game_canvas.itemconfig(self.canvas_frame, width = canvas_width)

    def mouse_scroll(self, event):
        # allows user to scroll with mouse if text is too long
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
