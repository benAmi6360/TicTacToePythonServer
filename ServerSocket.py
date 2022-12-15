"""Server socket class"""
import socket, time, game_info
from server import *


def log(msg):
    print("SERVER: " + time.strftime(r'%d|%m|%y, %H:%M'), msg)


class ServerSocket:
    PORT = 1729
    clients = []

    def __init__(self, listeners):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind(('0.0.0.0', self.PORT))
        log("Binding...")
        self._socket.listen(listeners)
        log("Listening to " + str(listeners) + " clients")
        for i in range(listeners):
            log("Waiting for client " + str(i))
            self.clients.append(self.accept_client())
        for client in self.clients:
            self.handle_client(client)


    def accept_client(self):
        client, addr = self._socket.accept()
        log("Accepted a client from " + str(addr))
        return client


    def handle_client(self, client):
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



serv = ServerSocket(1)