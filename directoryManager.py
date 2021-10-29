import os
from datetime import datetime

class FileAdmin:
    def __init__(self, nombre):
        self.nombre = nombre

    def receive_mensag(self, message):
        messageKernel = str(message)
        directory = os.getcwd()

        message= str(message).replace("b","")
        message= str(message).replace("'","")
        print(message)
        message=str(message).split(',')
        print(message)
        
        folderName = '\\' + message[3]

        try:
            if(message[0]=="CREATE"):
                now = datetime.now()
                os.mkdir(directory + folderName)
                print(directory + folderName)
                message = "INF,"+message[2]+","+message[1]+",OK,"+str(now)
                return message
            elif(message[0]=="DELETE"):
                os.rmdir(directory + folderName)
                message = "INF,"+message[2]+","+message[1]+",OK"+""
                return message
            elif(message[0] =="INFO"):
                message = "INFO,FILEADMIN,KERNEL,OK"
                return message
            elif(message[0] == "SAVE"):
                print(messageKernel)
                f = open ('logs.txt', 'a')
                f.write(messageKernel+'\n')
                f.close()
                return "1"
        except Exception as e:
            print("Ingreso Excepcion")
            cmd = "CREATE"
            src = message[2]
            dst = "GestorArch"
            message = cmd+","+src+","+dst+","+str(e)
            return message

