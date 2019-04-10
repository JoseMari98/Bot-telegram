import pika
import id_url


def mandarIdyUrl(id, url):
    objetoIdUrl = id_url
    objetoIdUrl.id = id
    objetoIdUrl.url = url

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    #channel.queue_declare(queue='IdUrl')
    channel.basic_publish(exchange="", routing_key='IdUrl', body= "AFUUUUUUUUUUUU")
    connection.close()

#def mandarDatosProducto()
