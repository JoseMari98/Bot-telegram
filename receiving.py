import pika
import Par

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

def callback(ch, method, properties, body): #imprime el contenido del mensaje
    objeto = Par.Par("", "")
    objeto.to_object(body)
    print("El id es " + str(objeto.id) + " y la url es " + objeto.url)


channel.basic_consume(queue='IdUrl', auto_ack=True, on_message_callback=callback)
channel.start_consuming()