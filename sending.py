import pika
from pymongo import MongoClient
from private import mongo

client = MongoClient(mongo)

db = MongoClient.test

collection = db.datos

db.test.find()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue=)
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
