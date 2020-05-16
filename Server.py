import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),9999))
s.listen(1)

while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has connected!")
    input_File= open("demo.txt",'r')
    dict={}
    for line in input_File:
        name = line.split("|")
        dict = {name[0]: (name[1], name[2], name[3])}
        print(dict)


    clientsocket.send(bytes("gvh","utf-8"))