import socket

host = 'localhost'
port = 8000

sock = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

sock.connect((host, port))
sock.send('Ping!'.encode())

message = sock.recv(4096)


print('Server said : ' + message.decode())

sock.close()
