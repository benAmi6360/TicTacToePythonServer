import socket
from window import GameWindow

def main():
    sock = socket.socket()
    sock.connect(('127.0.0.1', 1729))
    root = GameWindow('TicTacToe', sock)
    root.mainloop()


if __name__ == '__main__':
    main()