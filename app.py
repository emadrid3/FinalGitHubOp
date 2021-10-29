import os
from datetime import datetime
class App:
    def __init__(self,name):
        self.name = name

    def  get_pid(self,app):
        print("Ingreso",app)
        pids = []
        a = os.popen("tasklist").readlines()
        i = 0
        for x in a:
            try:
                t10 = x[0:77]
                t10 = t10.split(" ")
                t10 = [ele for ele in t10 if ele.strip()]
                if(app=="chrome"):
                    if(t10[0] =="chrome.exe"):
                        pids.append(t10[1])
                elif(app=="winword"):
                    if(t10[0] =="WINWORD.EXE"):
                        print("Winword, ingreso")
                        pids.append(t10[1])
            except Exception:
                pass
        return pids
    def receive_mensag(self,message):
        now = datetime.now()
        message= str(message).replace("b","")
        message= str(message).replace("'","")
        print(message)
        message=str(message).split(',')
        print(message)
        try:
            if(message[0]=="OPEN"):
                os.system("start "+message[3])
                print(self.get_pid(message[3]))
                message = "INF,"+message[2]+","+message[1]+",OK,"+str(now)+","+str(self.get_pid(message[3]))
                return message
            elif(message[0]=="CLOSE"):
                os.system("taskkill /F /PID "+message[3])
                message = "INF,"+message[2]+","+message[1]+",LOG: "+str(now)+"--> OK"
                return message
            elif(message[0]=="INFO"):
                print("info")
                return "INFO,APP,KERNEL,OK"
        except Exception as e:
                print("Ingreso a la exception")
                cmd = "INFO"
                src = message[2]
                dst = "GestorArch"  
                message = cmd+","+src+","+"APP"+","+str(e)
                return message
                #return message
            
    def action(message):
        if(message["command"]=="open"):
            os.command("start "+message["msg"])  
        elif(message["command"]=="close"):
            os.command(" ")
            
