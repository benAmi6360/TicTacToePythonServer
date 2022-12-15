"""A file that responsible of checking stuff like protocol"""
from game_info import GameBoard

def parse(data: str):
    """Takes a square cordinates and convert them to the protocol"""
    data = data.split(', ')
    lst = []
    for item in data:
        lst.append(item.replace(' ', ''))
    msg = '#'.join(lst) + '###'
    return msg.encode()


def parse_row_col(data: str):
    """Maps a message from the server to a dictionary"""
    data = data.split('#')
    milon = {}
    for item in data:
        try:
            item = item.split(':')
            milon[item[0]] = item[1]
        except:
            break
    return milon


def change_text(args):
    """The onClick commadn of the buttons"""
    game_info = GameBoard()
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
        cords = game_info.get_cords(map)
        btn = master.grid_slaves(row=cords[0], column=cords[1])
        btn[0].config(text='O', state='disabled')
    except:
        pass