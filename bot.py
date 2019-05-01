# -*- coding: utf-8 -*-


import telebot  # Librería de la API del bot.
from private import token
from pymongo import MongoClient
from private import mongo
from modificadores import insert, delete
from gets import obtenerNombre,obtenerPrecio

from telebot import types  # Tipos para la API del bot.

import time  # Librería para hacer que el programa que controla el bot no se acabe.

# Aqui definiremos aparte del Token, por ejemplo los ids de los grupos y pondríamos grupo= -XXXXX

bot = telebot.TeleBot(token)  # Creamos el objeto de nuestro bot.


#############################################

#Start

@bot.message_handler(commands=['start'])  # Indicamos que lo siguiente va a controlar el comando '/ayuda'
def command_start(m):  # Definimos una función que resuleva lo que necesitemos.
    bot.send_message(m.chat.id, "Bienvenido al amazon scraper")
    bot.send_message(m.chat.id, "Para scrapear un producto manda una url de amazon")
    bot.send_message(m.chat.id, "Para desuscribirte del producto usa el comando /leave+espacio+url")
    bot.send_message(m.chat.id, "Para ver tus productos activos usa el comando /productos")

    id = m.chat.id  # Guardamos el ID de la conversación para poder responder.

    client = MongoClient(mongo)
    db = client.test
    user = db.user
    ejem = {"id": id}
    usuario = user.find_one({"id":m.chat.id})

    if usuario == None:
        user.insert_one(ejem)
        bot.send_message(id, "Registro completado")

#Productos

@bot.message_handler(commands=['productos'])  # Indicamos que lo siguiente va a controlar el comando '/ayuda'
def command_productos(m):  # Definimos una función que resuleva lo que necesitemos.
    id = m.chat.id  # Guardamos el ID de la conversación para poder responder.

    client = MongoClient(mongo)
    db = client.test
    producto = db.producto
    esta_usuario = producto.find_one({"id_usuario": id})
    productos = producto.find({"id_usuario": id})

    if esta_usuario == None:
        bot.send_message(id, "No tiene ningun productos registrado")
    else:
        for p in productos:
            bot.send_message(id, "Nombre: " + p["nombre"] + " Precio: " + str(p["precio"]) + " euros")

#leave

@bot.message_handler(commands=['leave'])  # Indicamos que lo siguiente va a controlar el comando '/ayuda'
def command_leave(m):  # Definimos una función que resuleva lo que necesitemos.
    id = m.chat.id  # Guardamos el ID de la conversación para poder responder.

    client = MongoClient(mongo)
    db = client.test
    producto = db.producto
    tamano = len(m.text)
    texto = m.text[7:tamano]
    esta_producto = producto.find_one({"id_usuario": id, "url": texto})
    if esta_producto == None:
        bot.send_message(id, "Su producto no estaba registrado")
    else:
        delete(id, texto)
        bot.send_message(id, "Borrado con exito")


# Listener

def listener(messages):  # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.

    for m in messages:  # Por cada dato 'm' en el dato 'messages'
        client = MongoClient(mongo)
        db = client.test
        producto = db.producto

        tamano = len(m.text)
        texto = m.text[7:tamano]

        if m.content_type == 'text' and m.text != "/start" and m.text != "/leave " + texto and m.text != "/leave" and m.text != "/productos":
            url = m.text
            bot.send_message(m.chat.id, "Buscando su producto")

            #comprobamos que el usuario no tenga este producto en la base de datos
            name = obtenerNombre(url)
            esta_producto = producto.find_one({"id_usuario":m.chat.id, "nombre":name})
            if esta_producto != None:
                bot.send_message(m.chat.id, "El producto ya se esta analizando")
            else: #si no esta lo introducimos
                insert(m.chat.id, url)
                bot.send_message(m.chat.id, "Su producto llamado: " + name)
                bot.send_message(m.chat.id, "Tiene un precio actual de: " + str(obtenerPrecio(url)) + " euros")
                bot.send_message(m.chat.id, "Se le notificara cuando haya cambios de precio")

bot.set_update_listener(listener)  #Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
bot.polling()

while True: #No terminamos nuestro programa
    pass
