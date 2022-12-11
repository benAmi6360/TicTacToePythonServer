from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font
from functools import partial
from protocol import change_text


class GameWindow:
    board = []
    """Tic Tac Toe game window"""
    def __init__(self, title: str, socket) -> None:
        self.sock = socket
        self._root = self.create_window(title)
        self._mainframe = self.create_mainframe(self._root)
        self.create_button_grid(self._mainframe)


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


    def create_button_grid(self, mainframe):
        font = ('Ariel', '50')
        for i in range(3):
            for column in range(3):
                """Setup the button"""
                b = Button(mainframe, width=5, height=2, font=font)
                b.grid(row=i, column=column)
                self.board.append(b)
        for btn in self.board:
            p = partial(change_text, args=(btn, self.sock, self._mainframe))
            btn.config(command=p)


    def mainloop(self) -> None:
        self._root.mainloop()

