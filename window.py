from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk # pip install Pillow  
import tkinter.font as font
from functools import partial


root = Tk()
root.title("Tic Tac Toe")

root.resizable(0,0)

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

button_grid = []


def change_text(button):
    btn_text = StringVar()
    btn_text.set('X')
    button.config(textvariable=btn_text, state='disabled', compound=CENTER)
    root.update()



pixel = PhotoImage(width=1, height=1)
font = font=('Helvetica', '50')
for i in range(3):
    row = []
    for j in range(3):
        b = Button(mainframe, image=pixel, width=200, height=200, font=font)
        b.config(command=partial(change_text, b))
        row.append(b)
    button_grid.append(row)


for row, button_row in enumerate(button_grid):
    for column, button in enumerate(button_row):
        button.grid(row=row,column=column)

root.mainloop()