import pika
import Par

def mandarIdyUrl(id, url):


    par = Par.Par(id, url)

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.basic_publish(exchange="", routing_key='IdUrl', body= par.to_string())
    connection.close()

#def mandarDatosProducto():