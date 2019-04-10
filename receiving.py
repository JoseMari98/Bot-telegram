import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
#channel.queue_declare(queue='IdUrl')
def callback(ch, method, properties, body): #imprime el contenido del mensaje
    print("El id es" + body.id + " y la url es " + body.url)


channel.basic_consume(queue='IdUrl', auto_ack=True, on_message_callback=callback)
channel.start_consuming()