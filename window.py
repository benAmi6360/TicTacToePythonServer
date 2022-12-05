from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk # pip install Pillow
import tkinter.font as font
from functools import partial

def change_text(button):
    print('pressed')


class GameWindow:
    """Tic Tac Toe game window"""
    def create_window(self, title):
        """Initialize main window"""
        root = Tk()
        root.title(title)
        """Make window unable to resize"""
        root.resizable(0,0)
        return root


    def create_mainframe(self, root):
        """Create a mainframe"""
        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        return mainframe


    def create_button_grid(self, mainframe) -> list:
        """Creates an empty list for the buttons"""
        grid = []
        pixel = PhotoImage(width=1, height=1) # Creates a dummy pixel image (1x1)
        font = ('Ariel', '50')
        for i in range(3):
            """Creates a list for every row in grid"""
            row = []
            for column in range(3):
                """Setup the button"""
                b = Button(mainframe, relief=SUNKEN, image=pixel, width=200, height=200, font=font)
                b.config(command=partial(change_text, b))
                row.append(b)
            grid.append(row)
        return grid


    def add_buttons_to_grid(self, grid):
        for row_index, row in enumerate(grid):
            for column, button in enumerate(row):
                button.grid(row=row_index, column=column)


    def __init__(self, title: str) -> None:
        self._root = self.create_window(title)
        self._mainframe = self.create_mainframe(self._root)
        self._grid = self.create_button_grid(self._mainframe)
        self.add_buttons_to_grid(self._grid)



    def mainloop(self) -> None:
        self._root.mainloop()


window = GameWindow('TicTacToe')
window.mainloop()