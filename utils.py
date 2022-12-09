from tkinter import messagebox


def change_text(args):
    button, socket = args
    inf = button.grid_info()
    row, col = inf['row'], inf['column']
    messagebox.showinfo('Button pressed', f'button pressed at:\nrow:{row}, col:{col}')
    socket.send(f'row: {row}, col: {col}'.encode())
    print(row, col)