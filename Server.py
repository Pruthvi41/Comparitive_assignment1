import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),9999))
s.listen(1)

while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has connected!")
    clientsocket.send(bytes("hi","utf-8"))