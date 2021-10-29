from directoryManager import FileAdmin

fileadm = FileAdmin("fileadm")

import pika
host = "143.244.204.187" #"143.244.204.187"
port = "5672" #5672
user = "user" #user
pw = "password" #password

connection = pika.BlockingConnection(pika.ConnectionParameters(host, port, '/', 
pika.PlainCredentials(user, pw)))
channel = connection.channel()

def callback(ch, method, properties, body):
    message = fileadm.receive_mensag(body)
    print(body)
    print(message)
    if(message != "1"):
        channel.basic_publish(exchange='kernel', routing_key='kernel', body=message)
channel.basic_consume(queue="gestorarc", on_message_callback=callback, auto_ack=True)
channel.start_consuming()


