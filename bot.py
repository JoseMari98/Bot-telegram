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

# Listener

def listener(messages):  # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.

    for m in messages:  # Por cada dato 'm' en el dato 'messages'

        cid = m.chat.id  # El Cid es el identificador del chat los negativos son grupos y positivos los usuarios

        if cid > 0:

            mensaje = str(m.chat.first_name) + " [" + str(
                cid) + "]: " + m.text  # Si 'cid' es positivo, usaremos 'm.chat.first_name' para el nombre.


bot.set_update_listener(
    listener)  # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.