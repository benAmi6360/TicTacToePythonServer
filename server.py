import socket


def main():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('0.0.0.0', 1729))
    serv.listen(1)
    client, addr = serv.accept()
    while True:
        try:            
            data = client.recv(1024).decode()
            print(data)
            client.send(data.encode())
        except:
            break
    client.close()
    serv.close()


if __name__ == '__main__':
    main()
        