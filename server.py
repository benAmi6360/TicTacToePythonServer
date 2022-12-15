"""Server file of the TicTacToe game"""
import socket
import random
from game_info import GameBoard
from game_done_exception import GameDoneException

game_board = GameBoard()


def parse_data_to_dict(data):
    """Parses data received from client into a dictionary"""
    rowcol = {}
    for item in data.split('#'):
        try:
            item = item.split(':')
            rowcol[item[0]] = int(item[1])
        except Exception:
            break
    return rowcol



def get_random_cords():
    """Generate random cords for server response"""
    cords_dict = {
        'ROW': random.randint(0, 2),
        'COL': random.randint(0, 2)
    }
    try:
        while not game_board.validate_square(cords_dict):
            if game_board.is_board_full():
                raise GameDoneException
            cords_dict = {
                'ROW': random.randint(0, 2),
                'COL': random.randint(0, 2)
            }
    except GameDoneException:
        pass
    else:
        return game_board.get_cords(cords_dict)


def main():
    """Main entry for the file"""
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('0.0.0.0', 1729))
    serv.listen(1)
    client, addr = serv.accept()
    while True:
        try:
            if game_board.is_board_full():
                raise GameDoneException
            try:
                data = client.recv(1024).decode()
            except Exception as err:
                print(str(err))
            rowcol = parse_data_to_dict(data)
            while not game_board.validate_square(rowcol):
                data = client.recv(1024).decode()
                rowcol = parse_data_to_dict(data)
            client.send('GOTIT###'.encode())
            game_board.update_board(rowcol, who_took=False)
            while client.recv(1024).decode() != 'GOTIT###':
                continue
            try:
                cords = get_random_cords()
                outputdata = f'ROW:{cords[0]}#COL:{cords[1]}###'
                outputmap = {
                    'ROW': cords[0],
                    'COL': cords[1]
                }
                game_board.update_board(outputmap, True)
                client.send(outputdata.encode())
            except Exception as err:
                print(str(err))
        except GameDoneException:
            break
    client.close()
    serv.close()


if __name__ == '__main__':
    main()
