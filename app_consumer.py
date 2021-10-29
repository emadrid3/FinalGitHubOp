import pika
from app import App

host = SERVER_HOST
port = SERVER_PORT
user = SERVER_USER
pw =  SERVER_PW

connection = pika.BlockingConnection(pika.ConnectionParameters(host, port, '/', 
pika.PlainCredentials(user,pw)))
channel = connection.channel()
app = App("app")
def callback(ch, method, properties, body):
    print(body)
    print("Ingreso")
    messaje = app.receive_mensag(body)
    channel.basic_publish(exchange='kernel', routing_key="kernel", body=messaje)
channel.basic_consume(queue="app", on_message_callback=callback, auto_ack=True)
channel.start_consuming()
