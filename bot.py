# -*- coding: utf-8 -*-


import telebot  # Librería de la API del bot.
from private import token
from pymongo import MongoClient
from private import mongo

from telebot import types  # Tipos para la API del bot.

import time  # Librería para hacer que el programa que controla el bot no se acabe.

# Aqui definiremos aparte del Token, por ejemplo los ids de los grupos y pondríamos grupo= -XXXXX

bot = telebot.TeleBot(token)  # Creamos el objeto de nuestro bot.


#############################################

#Start

@bot.message_handler(commands=['start'])  # Indicamos que lo siguiente va a controlar el comando '/ayuda'
def command_start(m):  # Definimos una función que resuleva lo que necesitemos.

    id = m.chat.id  # Guardamos el ID de la conversación para poder responder.

    bot.send_message(id, "Ya estas registrado")  # Enviando ...

    client = MongoClient(mongo)
    db = client.test
    collection = db.user
    ejem = {"id": id}
    id_bd = collection.insert_one(ejem).inserted_id

# Listener

def listener(messages):  # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.

    for m in messages:  # Por cada dato 'm' en el dato 'messages'
        client = MongoClient(mongo)
        db = client.test
        collection = db.user
        try:
            id_bd = collection.find({"id":m.chat.id})
        except:
            print("error")

        text = m.text
        bot.send_message(m.chat.id, "Buscando su producto")
        #mandarlo por la cola de mensajes


bot.set_update_listener(listener)  #Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
bot.polling()