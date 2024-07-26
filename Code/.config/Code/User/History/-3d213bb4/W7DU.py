import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from Scripts.input_logic import InputLogic


# TODO - 1. Create the GUI 2. Build the algorithm


class GUI:
    def __init__(self, size: tuple):
        self.app = ttk.Window(title="Wordle Bot", themename="darkly")
        self.app.geometry(f"{size[0]}x{size[1]}")
        self.app.maxsize(size[0], size[1])
        self.app.minsize(size[0], size[1])
        self.logic = InputLogic(self)

    def main_word_frame(self, width, height, font: str):
        # Main Word
        self.side = "left"

        self.main_word = ttk.Frame(master=self.app)

        self.letStr1 = ttk.StringVar()
        self.letter1 = ttk.Entry(
            master=self.main_word, width=width, font=font, textvariable=self.letStr1
        )
        self.letStr1.trace_add(
            "write",
            lambda var, index, mode: self.logic.one_word(
                var=var, index=index, mode=mode, strvar=self.letStr1, focus=self.letter2
            ),
        )

        self.letStr2 = ttk.StringVar()
        self.letter2 = ttk.Entry(
            master=self.main_word, width=width, font=font, textvariable=self.letStr2
        )
        self.letStr1.trace_add(
            "write",
            lambda var, index, mode: self.logic.one_word(
                var=var, index=index, mode=mode, strvar=self.letStr1, focus=self.letter2
            ),
        )

        self.letStr3 = ttk.StringVar()
        self.letter3 = ttk.Entry(
            master=self.main_word, width=width, font=font, textvariable=self.letStr3
        )
        self.letStr1.trace_add(
            "write",
            lambda var, index, mode: self.logic.one_word(
                var=var, index=index, mode=mode, strvar=self.letStr1, focus=self.letter2
            ),
        )

        self.letStr4 = ttk.StringVar()
        self.letter4 = ttk.Entry(
            master=self.main_word, width=width, font=font, textvariable=self.letStr4
        )
        self.letStr1.trace_add(
            "write",
            lambda var, index, mode: self.logic.one_word(
                var=var, index=index, mode=mode, strvar=self.letStr1, focus=self.letter2
            ),
        )

        self.letStr5 = ttk.StringVar()
        self.letter5 = ttk.Entry(
            master=self.main_word,
            width=width,
            font=font,
            textvariable=self.letStr5,
        )
        self.letStr5.trace_add(
            "write",
            lambda var, index, mode: self.logic.one_word(
                var=var, index=index, mode=mode, strvar=self.letStr1, focus=self.letter2
            ),
        )

        self.letter1.pack(side=self.side, padx=5)
        self.letter2.pack(side=self.side, padx=5)
        self.letter3.pack(side=self.side, padx=5)
        self.letter4.pack(side=self.side, padx=5)
        self.letter5.pack(side=self.side, padx=5)
        self.main_word.pack(pady=20)

    def good_words_frame(self):
        # Good Words
        self.good = ttk.Frame(master=self.app)
        self.good_word = ttk.Label(
            master=self.good, text="Good Letters", font="Segoe_UI 12 bold"
        )
        letters = ttk.StringVar()
        letters_entry = ttk.Entry(
            master=self.good, font="Segoe_UI", textvariable=letters
        )

        self.good_word.pack(side="left", padx=10)
        letters_entry.pack(side="left", padx=10)
        self.good.pack(pady=20)

    def bad_word_frame(self):
        # Bad Words
        self.bad = ttk.Frame(master=self.app)
        self.bad_word = ttk.Label(
            master=self.bad, text="Bad Letters", font="Segoe_UI 12 bold"
        )
        letters = ttk.StringVar()
        letters_entry = ttk.Entry(
            master=self.bad, font="Segoe_UI", textvariable=letters
        )

        self.bad_word.pack(side="left", padx=10)
        letters_entry.pack(side="left", padx=10)
        self.bad.pack(pady=20)

    def search_frame(self):
        # Search Button
        self.search = ttk.Frame(master=self.app)
        self.search_button = ttk.Button(
            master=self.search,
            text="Search",
            width=15,
        )
        self.wrong = ttk.Button(master=self.search, text="X", width=2)
        self.right = ttk.Button(master=self.search, text="Y", width=2)
        self.wrong.pack(side="left", padx=20)
        self.search_button.pack(side="left", padx=20)
        self.right.pack(side="left", padx=20)
        self.search.pack(pady=20)

    def run(self):
        self.main_word_frame(5, 3, "Segoe_UI 18 bold")
        self.good_words_frame()
        self.bad_word_frame()
        self.search_frame()

        self.app.mainloop()





if __name__ == "__main__":
    gui = GUI((1000, 600))
    gui.run()
