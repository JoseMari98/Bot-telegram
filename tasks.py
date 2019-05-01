from celery import Celery
from celery.schedules import crontab
from pymongo import MongoClient
from private import mongo, token
import telebot
from gets import obtenerPrecio, obtenerNombre

bot = telebot.TeleBot(token)

# Crea usando RPC para devolver los datos, y el broker AMQP
app = Celery("tasks", backend="rpc://", broker="pyamqp://guest@localhost//")

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Se llama cada 4 horas
    #sender.add_periodic_task(crontab(minute=0, hour='*/1'), analisis())
    sender.add_periodic_task(10, analisis.s())

@app.task
def analisis():
    print("hola")
    client = MongoClient(mongo)
    db = client.test
    producto = db.producto
    productos = producto.find()

    for p in productos:
        precio_actual = obtenerPrecio(p["url"])
        if precio_actual != p["precio"]:
            producto.update_one({"id_usuario": p["id_usuario"],"nombre": p["nombre"]}, {"$set": {"precio": precio_actual}})
            bot.send_message(p["id_usuario"], "El precio de: " + p["nombre"] + " ahora es de: " + str(precio_actual) + " euros")
