import socket
from window import GameWindow
from protocol import parse, parse_row_col
from server import get_cords



def main():
    sock = socket.socket()
    sock.connect(('10.92.13.171', 1729))
    root = GameWindow('TicTacToe', sock)
    root.mainloop()


if __name__ == '__main__':
    main()