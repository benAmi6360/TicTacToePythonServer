"""Client file of the TicTacToe project"""
import socket
from window import GameWindow



def main():
    """Main entry for the file"""
    ip = input("Enter the server address: ")
    sock = socket.socket()
    sock.connect((ip, 1729))
    root = GameWindow('TicTacToe', sock)
    root.mainloop()


if __name__ == '__main__':
    main()
