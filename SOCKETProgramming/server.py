import socket

port = 8000

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

sock.bind(('', port))
sock.listen(1)

hostname = socket.gethostbyname(socket.gethostname())
print('Server started at host: ' + hostname + ' on port: ' + str(port))

client_sock, addr = sock.accept()
message = client_sock.recv(4096)
print('client said : ' + message.decode())

client_sock.send('pong!'.encode())

sock.close()
