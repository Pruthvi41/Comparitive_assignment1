import socket,time,sys
print("Initialising....\n")
time.sleep(1)

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = input(str("Enter server address: "))
port = 9999
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

#s.send(name.encode())
#s_name = s.recv(1024)
#s_name = s_name.decode()

while True:
    print("Python DB Menu\n1. Find customer\n2. Add customer\n3. Delete customer\n4. Update customer age\n5. Update customer address\n6. Update customer phone\n7. Print report\n8. Exit")
    select_Option=input("Select: ")
    s.send(bytes(select_Option,"utf-8"))
    name=s.recv(1024)
    name=name.decode("utf-8")
    print(name)            

            
    #s.send(message.encode())


    