import socket



class customer:
    def __init__(self,name,age,address,phone):
        self.name=name
        self.age=age
        self.address=address
        self.phone=phone

class DBSever:
    def __init__(self):
        #
        #load from file
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((socket.gethostname(),1254))
        self.data =self.load()

          

    def load(self):
        filename="data.txt"
        f=open(filename,"r")
        lines=f.readlines()
        dictdata = {}
        for line in lines:
            data=line.split('|')
            #print(type(data))
            dictdata[data[0].lower()]=[temp.strip() for temp in data]
        f.close()
        return dictdata

    
    def test(self):
        pass

DbSever = DBSever()
DbSever.server.listen(1)
#print(DbSever.data)

client=None
request_data=""
req_data=[]

def validate_customer(name):
    if name.lower() in DbSever.data.keys():
        return True
    else:
        return False
    
def find_customer():
    #find the customer 
    #rec_data=request_data.split(",")
    if validate_customer(req_data[1]):
        res=DbSever.data[req_data[1].lower()]
        data="Name:"+res[0]+","+" age:"+res[1]+","+" address:"+res[2]+","+" phone_number:"+res[3]
    else:
        data ="customer not found"
    return data
def add_customer():
    ## add new customer to the data list 
    name =req_data[1]
    age =req_data[2]
    address=req_data[3]
    phone_number=req_data[4]
    DbSever.data[name.lower()]=[name,age,address,phone_number]
    return "Sucessfully added the customer"
def delete_customer():
    ##delete customer from dict
    if validate_customer(req_data[1]):
        del DbSever.data[req_data[1].lower()]
        data = "Sucessfully deleted the customer record "+req_data[1]
    else:
        data ="customer not found"

    return data
def update_customer_age():
    #update customers age 
    if validate_customer(req_data[1]):
        DbSever.data[req_data[1].lower()][1]=req_data[2]
        data = "Sucessfully updated age for the  record "+req_data[1]
    else:
        data ="customer not found"

    return data
def update_customer_address():
    #update cutomer address 
    if validate_customer(req_data[1]):
        DbSever.data[req_data[1].lower()][2]=req_data[2]
        data = "Sucessfully updated age for the  record "+req_data[1]
    else:
        data ="customer not found"

    return data
def update_customer_number():
    #update phone number of the customer 
    if validate_customer(req_data[1]):
        DbSever.data[req_data[1].lower()][3]=req_data[2]
        data = "Sucessfully updated age for the  record "+req_data[1]
    else:
        data ="customer not found"

    return data
def print_report():
    #Todo
    #send report 
    #sort the dict with keys and send the values in the keys
    #ordered keys 
    #print("In print method")
    data={k: v for k, v in sorted(DbSever.data.items(), key=lambda item: item[0])}
    data =[v for v in data.values()]

    return str(data)
def sys_exit():
    #save data in file data.txt
    #print("here")
    filename="data.txt"
    f=open(filename,"r+")
    f.truncate(0)
    f.close()
    f= open(filename,"w+") 
    delim='|'
    for line in DbSever.data.values():
        templine=delim.join(line)
        f.write(templine+"\n")
    f.close()
    client=None

    print("end")
    return None
        


def option_to_function(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "nothing")
    # Execute the function
    return func()
switcher ={
    1:find_customer,
    2:add_customer,
    3:delete_customer,
    4:update_customer_age,
    5:update_customer_address,
    6:update_customer_number,
    7:print_report,
    8:sys_exit
}

while True:
    if client is None:
        print("connection None")
        client,address = DbSever.server.accept()
        print("connection established ")
    else:
        received_data = client.recv(1024)
        #print(received_data)
        ##
        request_data=received_data.decode()
        #print(request_data)
        if(request_data.strip()):
            req_data=request_data.split(",")
            #print(req_data[0])
            respose=option_to_function(int(req_data[0]))
            if(respose is not None):
                #print("In response")
                client.send(respose.encode())
        
        



#  if c is None:
#        # Halts
#        print('[Waiting for connection...]')
#        c, addr = s.accept()
#        print('Got connection from', addr)
#    else:
#        # Halts
#        print('[Waiting for response...]')
#        print(c.recv(1024))
#        q = input("Enter something to this client: ")
#        c.send(q.encode())
