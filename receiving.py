import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

def callback(ch, method, properties, body): #imprime el contenido del mensaje
    print(" [x] Received %r" % body)

channel.basic_consume(queue='hello', #indicamos que vamos a recivir un mensaje de la cola hello
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()