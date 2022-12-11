import time
from server import get_cords

def parse(data: str):
    data = data.split(', ')
    lst = []
    for item in data:
        lst.append(item.replace(' ', ''))
    msg = '#'.join(lst) + '###'
    return msg.encode()


def parse_row_col(data: str):
    data = data.split('#')
    map = {}
    for item in data:
        try:
            item = item.split(':')
            map[item[0]] = item[1]
        except:
            break
    return map


def get_btn_with_cords(cords, board):
    for row in board:
        for btn in row:
            inf = btn.grid_info()
            row, col = inf['row'], inf['column']
            if row == cords[0] and col == cords[1]:
                return btn


def change_text(args):
    try:
        button, socket, master = args
        inf = button.grid_info()
        row, col = inf['row'], inf['column']
        socket.sendall(parse(f'ROW: {row}, COL: {col}'))
        data = socket.recv(1024)
        while data != b'GOTIT###':
            data = socket.recv(1024).decode()
        button.config(text='X', state='disabled')
        socket.send('GOTIT###'.encode())
        data = socket.recv(1024).decode()
        map = parse_row_col(data)
        cords = get_cords(map)
        btn = master.grid_slaves(row=cords[0], column=cords[1])
        btn[0].config(text='O', state='disabled')
    except:
        pass