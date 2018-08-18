import socket

port = 8000

# we'll send this message before closing connection
# so that other side can close connection as well
CLOSE = b'--close--'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def host():
    sock.bind(('', port))
    sock.listen(1)

    # is supposed to return the local IP of the computer
    # might not always work
    hostname = socket.gethostbyname(socket.gethostname())
    print('Server started at host: ' + hostname + ' on port: ' + str(port))

    client_sock, addr = sock.accept()

    print('\nConnection established. Type and press enter to send message.')
    print('Press Ctrl+C to end conversation\n')

    while True:
        try:
            message = client_sock.recv(4096)
            print('Friend said: ', message.decode())

            # closing message received from client
            if message == CLOSE:
                client_sock.close()
                sock.close()
                break

            reply = input('I say: ')
            client_sock.send(reply.encode())
        except KeyboardInterrupt:
            # Ctrl + C was pressed
            # Send closing message before closing socket
            client_sock.send(CLOSE)
            client_sock.close()
            sock.close()
            break


def join():
    sock.connect((hostname, port))

    print('\nConnection established. Type and press enter to send message')
    print('Press Ctrl+C to end conversation\n')

    while True:
        try:
            message = input('I say: ')
            sock.send(message.encode())
            reply = sock.recv(4096)
            print('Friend said: ', reply.decode())

            if reply == CLOSE:
                sock.close()
                break
        except KeyboardInterrupt:
            # Ctrl + C pressed
            # Send closing message before closing socket
            sock.send(CLOSE)
            sock.close()
            break


if __name__ == '__main__':
    choice = input('1. Host\n2. Join\nYour choice: ')
    if choice[0] in '1Hh':
        host()
    else:
        hostname = input('Enter host IP or hostname: ')
        join()
