import socket
import random
from MarkType import MarkType
from GameDoneException import GameDoneException


board = []


def initialize_grid():
    grid = []
    for _ in range(3):
        row = []
        for _ in range(3):
            row.append(MarkType.FREE)
        grid.append(row)
    return grid


def is_board_full():
    for row in board:
        for square in row:
            if square == MarkType.FREE:
                return False
    return True


def get_cords(map):
    cords = []
    for key in map.keys():
        cords.append(int(map[key]))
    return cords

def update_board(map: dict) -> None:
    global board
    cords = get_cords(map)
    board[cords[0]][cords[1]] = MarkType.TAKEN


def parse_data_to_dict(data):
    rowcol = {}
    for item in data.split('#'):
        try:
            item = item.split(':')
            rowcol[item[0]] = int(item[1])
        except:
            break
    return rowcol


def validate_square(map: dict) -> bool:
    cords = get_cords(map)
    return board[cords[0]][cords[1]] == MarkType.FREE


def get_random_cords():
    map = {
        'ROW': random.randint(0, 2),
        'COL': random.randint(0, 2)
    }
    try:
        while not validate_square(map):
            if is_board_full():
                raise GameDoneException
            map = {
                'ROW': random.randint(0, 2),
                'COL': random.randint(0, 2)
            }
    except:
        pass
    else:
        return get_cords(map)



def main():
    global board
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('0.0.0.0', 1729))
    serv.listen(1)
    board = initialize_grid()
    client, addr = serv.accept()
    while True:
        try:
            if is_board_full():
                raise GameDoneException
            try:
                data = client.recv(1024).decode()
            except Exception as e:
                print(str(e))
            rowcol = parse_data_to_dict(data)
            while not validate_square(rowcol):
                data = client.recv(1024).decode()
                rowcol = parse_data_to_dict(data)
            client.send('GOTIT###'.encode())
            update_board(rowcol)
            while client.recv(1024).decode() != 'GOTIT###':
                continue
            try:
                cords = get_random_cords()
                outputdata = f'ROW:{cords[0]}#COL:{cords[1]}###'
                outputmap = {
                    'ROW': cords[0],
                    'COL': cords[1]
                }
                update_board(outputmap)
                print(board)
                client.send(outputdata.encode())
            except:
                break
        except GameDoneException:
            client.send("Game#Done###".encode())
            break
    client.close()
    serv.close()


if __name__ == '__main__':
    main()
