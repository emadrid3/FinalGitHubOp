class Kernel:
    def __init__(self):
        return
    
    def  receive_mensag(message):
        message= str(message).replace("b","")
        message= str(message).replace("'","")
        print(message)
        message=str(message).split(',')
        print(message)
        if(message[2]=="GUI"):
            return "gui"
        elif (message[2]=="FILEADMIN"):
            return "gestorarc"
        elif(message[2]=="APP"):
            return "app"
            
            
    def send_chain_app(message):
        print("jairo funciona")
    
    def send_chain_file_managment(message):
        return(message)
    
    def request_chain(message):
        return
        
    def stop_exc(message):
        return
    
        