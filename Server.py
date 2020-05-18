import time, socket, sys
print("Initialising....\n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 9999
s.bind((host, port))
print(host, "(", ip, ")\n")           
s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")
input_File= open("demo.txt",'r')
dict={}
for line in input_File:
    name = line.split("|")
    dict[name[0]]=(name[1:])

#conn.send(name.encode())


while True:
    s_name = conn.recv(1024)
    s_name = s_name.decode("utf-8")
    print(s_name)
    conn.send(bytes("Hello","utf-8"))
    #conn.send(bytes("gvh","utf-8"))
    #conn.send(message.encode())
    #message = conn.recv(1024)
    #message = message.decode()
    #print(s_name, ":", message)
