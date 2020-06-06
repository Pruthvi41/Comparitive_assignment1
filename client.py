import socket
import sys
class client():
    def __init__(self):
        #
        #load from file
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect((socket.gethostname(),1254))

    #def exeoptions(self):
     #   print("choose from following: \n 1)find customer \n 2)add customer \n 3)delete customer \n4)update customer age \n5)update cutomer address\n6)update customer phone number\n 7)print report \n 8)exit")
client = client()



def find_customer():
    cus_name = input("please enter the customer : ")
    return cus_name
def add_customer():
    cus_name = input("please enter the customer name: ")
    cus_age = input("please enter the customer age : ")
    cus_address = input("please enter the customer address: ")
    cus_phone=input("please enter the customer phone number : ")
    # print(not cus_name)
    # print(cus_age.isdigit())
    data=""
    if cus_name and (not cus_age or cus_age.isdigit()):
        data = cus_name+","+cus_age+","+cus_address+","+cus_phone
    return data
def delete_customer():
    cus_name = input("please enter the customer name to delete : ")
    return cus_name
def update_customer_age():
    cus_name = input("please enter the customer name to update age  : ")
    cus_age=input("please enter age to update ")
    if(cus_age.isdigit() or not cus_age):
        data=cus_name+","+cus_age
        return data
    else:
        print("enter a valid age")
        
    
def update_customer_address():
    cus_name = input("please enter the customer name to update address  : ")
    cus_address=input("please enter address to update ")
    data=cus_name+","+cus_address
    return data
def update_customer_number():
    cus_name = input("please enter the customer name to update phone number  : ")
    cus_phone=input("please enter phone number to update ")
    
    data=cus_name+","+cus_phone
    return data
def print_report():
    print_data=eval(rec_data)
    #print(print_data)
    heading="|" + "Name".center(20)+"|"+"Age".center(5)+"|"+"Address".center(40)+"|"+"phone number".center(8)+"|"
    print("###############################################################################################")
    print(heading)
    
    print("###############################################################################################")
    for temp in print_data:
        line= "|" +str(temp[0]).ljust(20)+"|"+str(temp[1]).ljust(5) +"|"+ str(temp[2]).ljust(40)+"|"+ str(temp[3]).ljust(8)  +"|"  
        print(line)
    print("#################################################################################################")
    
def sys_exit():
    print("good bye")
    client.client.close()
    sys.exit()
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
    print("")
    print("choose from following: \n 1)find customer \n 2)add customer \n 3)delete customer \n 4)update customer age \n 5)update cutomer address\n 6)update customer phone number\n 7)print report \n 8)exit")
    print("please enter option below: ")
    option =int(input())
    if not option>=1 and option<=8:
        continue
    else:
        if option < 7:
            sendmsg=option_to_function(option)
            if sendmsg:
                sendmsg=str(option)+','+sendmsg
                client.client.send(sendmsg.encode())
                rec_data=client.client.recv(1024).decode()
                print(rec_data)
            else: 
                print("please enter valid details")
                print("")
                continue
        else:
            
            sendmsg=str(option)+ "," + "dummy"
            if option==7:
                client.client.send(sendmsg.encode())
                rec_data=client.client.recv(2048).decode()
                
                option_to_function(option)
            else:
                
                client.client.send(sendmsg.encode())
                option_to_function(option)




        




