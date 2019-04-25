# -*- coding: utf-8 -*-


import telebot  # Librería de la API del bot.
from private import token
from pymongo import MongoClient
from private import mongo
from insert import insert
from gets import obtenerNombre,obtenerPrecio

from telebot import types  # Tipos para la API del bot.

import time  # Librería para hacer que el programa que controla el bot no se acabe.

# Aqui definiremos aparte del Token, por ejemplo los ids de los grupos y pondríamos grupo= -XXXXX

bot = telebot.TeleBot(token)  # Creamos el objeto de nuestro bot.


#############################################

#Start

@bot.message_handler(commands=['start'])  # Indicamos que lo siguiente va a controlar el comando '/ayuda'
def command_start(m):  # Definimos una función que resuleva lo que necesitemos.

    id = m.chat.id  # Guardamos el ID de la conversación para poder responder.

    client = MongoClient(mongo)
    db = client.test
    user = db.user
    ejem = {"id": id}
    try:
        id_bd = user.find_one({"id":m.chat.id})
    except:
        print("error")
    if id_bd["id"] != m.chat.id:
        user.insert_one(ejem)
        bot.send_message(id, "Registro completado")
    else:
        bot.send_message(id, "Ya estabas registrado previamente")

# Listener

def listener(messages):  # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.

    for m in messages:  # Por cada dato 'm' en el dato 'messages'
        client = MongoClient(mongo)
        db = client.test
        #user = db.user
        producto = db.producto
        #try:
        #    id_bd = user.find({"id":m.chat.id})
        #except:
        #    print("error")
        if m.content_type == 'text' and m.text != "/start":
            url = m.text
            bot.send_message(m.chat.id, "Buscando su producto")

            #comprobamos que el usuario no tenga este producto en la base de datos
            name = obtenerNombre(url)
            esta_producto = producto.find_one({"id_usuario":m.chat.id, "nombre":name})
            if esta_producto != None:
                bot.send_message(m.chat.id, "El producto ya se esta analizando")
            else: #si no esta lo introducimos
                insert(m.chat.id, url)
                bot.send_message(m.chat.id, "Su producto llamado: " + name + "Tiene un precio actual de: " + obtenerPrecio(url) + "Se le notificara cuando haya cambios de precio")


bot.set_update_listener(listener)  #Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
bot.polling()

while True: #No terminamos nuestro programa
    pass
