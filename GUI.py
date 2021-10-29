import tkinter
from tkinter.constants import BOTH, LEFT, YES
from datetime import datetime
import os
import pika
from threading import *
import time

host = "143.244.204.187" #"143.244.204.187"
port = "5672" #5672
user = "user" #user
pw = "password" #password

pid = ""

connection = pika.BlockingConnection(pika.ConnectionParameters(host, port, '/', pika.PlainCredentials(user, pw)))
channel = connection.channel()
def hilo1():
    mainWindow = tkinter.Tk()
    mainWindow.geometry("500x500")
    mainWindow.resizable(0, 0)

    wordPanel = tkinter.Frame(master=mainWindow, width=500, height=200)
    wordPanel.grid(row=0, column=0, columnspan=2, rowspan=2, ipady=80)

    chromePanel = tkinter.Frame(master=mainWindow, width=500, height=200)
    chromePanel.grid(row=0, column=2, columnspan=2, rowspan=2, ipady=80)

    processPanel = tkinter.Frame(master=mainWindow, width=1000, height=200)
    processPanel.grid(row=2, column=0, columnspan=4, rowspan=2, ipady=10)

    createDirectoryPanel = tkinter.Frame(master=mainWindow, width=500, height=200)
    createDirectoryPanel.grid(row=4, column=0, columnspan=2, rowspan=2, ipady=20, pady=80)

    deleteDirectoryPanel = tkinter.Frame(master=mainWindow, width=500, height=200)
    deleteDirectoryPanel.grid(row=4, column=2, columnspan=2, rowspan=2, ipady=20)

    widthPanel = tkinter.Frame(master=mainWindow, width=500, height=200)
    widthPanel.grid(row=6, column=0, columnspan=4, rowspan=2)


    # APLICACIONES
    def openWord():
        response = "OPEN,GUI,APP,winword,Log: " + \
            str(datetime.now()) + " -> Open Word"
        channel.basic_publish(exchange='kernel', routing_key='kernel', body=response)
        print("Runnning Producer Application...")
        print(" [x] Sent 'Open Word...!'")
        print(response)


    openWordBTN = tkinter.Button(
        master=wordPanel, text="Open Word", command=lambda: openWord())
    openWordBTN.pack(side=LEFT, padx=10)

    def closeWord():
        print(pid)
        response = "CLOSE,GUI,APP,"+pid+",Log: " + \
            str(datetime.now()) + " -> Close Word"
        channel.basic_publish(exchange='kernel', routing_key='kernel', body=response)
        print("Runnning Producer Application...")
        print(" [x] Sent 'Close Word...!'")
        print(response)


    closeWordBTN = tkinter.Button(
        wordPanel, text="Close Word", command=lambda: closeWord())
    closeWordBTN.pack(side=LEFT, padx=10)


    def openChrome():
        response = "OPEN,GUI,APP,chrome,Log: " + \
            str(datetime.now()) + " -> Open chrome"
        channel.basic_publish(exchange='kernel', routing_key='kernel', body=response)
        print("Runnning Producer Application...")
        print(" [x] Sent 'Open Chrome...!'")
        print(response)


    openChromeBTN = tkinter.Button(
        chromePanel, text="Open Chrome", command=lambda: openChrome())
    openChromeBTN.pack(side=LEFT, padx=10)


    def closeChrome():
        folderName = closeChromeInput.get()
        response = "CLOSE,GUI,APP,"+str(folderName)+",Log: " + \
            str(datetime.now()) + " -> Close crhome"
        channel.basic_publish(exchange='kernel', routing_key='kernel', body=response)
        print("Runnning Producer Application...")
        print(" [x] Sent 'Close Chrome...!'")
        print(response)

    closeChromeLabel = tkinter.Label(
    master=chromePanel, text="Number of pid:")
    closeChromeLabel.pack()

    closeChromeInput = tkinter.Entry(master=chromePanel)
    closeChromeInput.pack()

    closeChromeBTN = tkinter.Button(
        chromePanel, text="Close Chrome", command=lambda: closeChrome())
    closeChromeBTN.pack(side=LEFT, padx=10)


    # PROCESOS
    def startApp():
        response = "OPEN,GUI,KERNEL,APP,Log: " + \
            str(datetime.now()) + " -> Init app process"
        channel.basic_publish(exchange='kernel', routing_key='kernel', body=response)
        print("Runnning Producer Application...")
        print(" [x] Sent 'Start App...!'")
        print(response)


    startAppBTN = tkinter.Button(
        processPanel, text="Start App", command=lambda: startApp())
    startAppBTN.pack(side=LEFT, padx=10)


    def stopApp():
        response = "CLOSE,GUI,KERNEL,APP,Log: " + \
            str(datetime.now()) + " -> Stop app process"
        channel.basic_publish(exchange='kernel', routing_key='kernel', body=response)
        print("Runnning Producer Application...")
        print(" [x] Sent 'Stop App...!'")
        print(response)


    stopAppBTN = tkinter.Button(
        processPanel, text="Stop App", command=lambda: stopApp())
    stopAppBTN.pack(side=LEFT, padx=10)


    # CARPETAS
    def createDir():
        directory = os.getcwd()
        folderName = createDirInput.get()
        print(folderName)
        response = "CREATE,GUI,FILEADMIN,"+str(folderName)+",Log: " + str(
            datetime.now()) + " -> Create \"" + str(folderName) + "\" directory"
        channel.basic_publish(exchange='kernel', routing_key='kernel', body=response)
        print("Runnning Producer Application...")
        print(" [x] Sent 'Create Dir...!'")
        print(response)


    createDirLabel = tkinter.Label(
        master=createDirectoryPanel, text="Name for new directory:")
    createDirLabel.pack()

    createDirInput = tkinter.Entry(master=createDirectoryPanel)
    createDirInput.pack()

    createDirBTN = tkinter.Button(
        master=createDirectoryPanel, text="Create directory", command=lambda: createDir())
    createDirBTN.pack(pady=10)

    def deleteDir():
        directory = os.getcwd()
        folderName = deleteDirInput.get()
        response = "DELETE,GUI,FILEADMIN,"+str(folderName)+",Log: " + str(
            datetime.now()) + " -> Delete \"" + str(folderName) + "\" directory"
        channel.basic_publish(exchange='kernel', routing_key='kernel', body=response)
        print("Runnning Producer Application...")
        print(" [x] Sent 'Delete Dir...!'")
        print(response)


    deleteDirLabel = tkinter.Label(
        master=deleteDirectoryPanel, text="Name of directory:")
    deleteDirLabel.pack()

    deleteDirInput = tkinter.Entry(master=deleteDirectoryPanel)
    deleteDirInput.pack()

    deleteDirBTN = tkinter.Button(
        master=deleteDirectoryPanel, text="Delete directory", command=lambda: deleteDir())
    deleteDirBTN.pack(pady=10)
    time.sleep(3)
    mainWindow.mainloop()

def hilo2():
    def callback(ch, method, properties, body):
        #print(body)
        receive_mensag(body)

    channel.basic_consume(queue="gui", on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
    time.sleep(3)

def  receive_mensag(message):
        print(message)
        global pid
        message= str(message).replace("b","")
        message= str(message).replace("'","")
        #print(message)
        message=str(message).split(',')
        message = message[-1].replace('"','').replace("[",'').replace("]",'')
        pid = message
        print(pid)


t = Timer(5.0, hilo1)
t2 = Timer(3.0, hilo2)
# Ejecutar los hilos
t.start()
t2.start()