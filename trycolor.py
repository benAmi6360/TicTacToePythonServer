from tkinter import *
import tkinter as tkinter
from tkinter import PhotoImage
from PIL import Image, ImageTk
 
root = tkinter.Tk()
xx = tkinter.Button(root, text='Hello', bg="white", fg="blue", image=PhotoImage(file='/cross.png'), width=200, height=200)
xx.pack()
root.mainloop()