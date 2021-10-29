import pika
from kernel import Kernel
from datetime import datetime

host = SERVER_HOST
port = SERVER_PORT
user = SERVER_USER
pw =  SERVER_PW

def state_send(state):
    message = ""
    date = datetime.now()
    stat_log = ""
    if(state==1):
        state_log="--> open "
    else:
        state_log ="--> close"
    message = "INFO,KERNEL,"
    log = ",LOG:"+str(date)+state_log
    channel.basic_publish(exchange='kernel', routing_key="app", body=message+"APP,"+str(state)+log+"app")
    channel.basic_publish(exchange='kernel', routing_key="gui", body=message+"GUI,"+str(state)+log+"gui")
    channel.basic_publish(exchange='kernel', routing_key="gestorarc", body=message+"FILEADMIN"+str(state)+log+"fileadmin")
connection = pika.BlockingConnection(pika.ConnectionParameters(host, port, '/', 
pika.PlainCredentials(user,pw)))
channel = connection.channel()
kernel = Kernel()
state_send(1)
def callback(ch, method, properties, body):
    if(str(body)!="b'1'"):
       
        key = Kernel.receive_mensag(body)
        print("kernel is send menssage to "+str(key))
        channel.basic_publish(exchange='kernel', routing_key=str(key), body=body)
    body = str(body).replace("'","")
    channel.basic_publish(exchange='kernel', routing_key="gestorarc", body="SAVE,"+str(body))
        
channel.basic_consume(queue="kernel", on_message_callback=callback, auto_ack=True)
channel.start_consuming()
state_send(0)
