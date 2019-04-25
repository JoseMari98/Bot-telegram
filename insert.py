from pymongo import MongoClient
from private import mongo
from gets import obtenerPrecio,obtenerNombre
import requests
from bs4 import BeautifulSoup

def insert(id, url):
    name = obtenerNombre(url)
    price = obtenerPrecio(url)

    client = MongoClient(mongo)
    db = client.test
    collection = db.producto
    consulta = {"id_usuario": id, "nombre": name, "precio": price, "url": url}
    collection.insert_one(consulta)