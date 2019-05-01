import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from pymongo import MongoClient
from private import mongo
from gets import obtenerNombre, obtenerPrecio

#url = "https://www.amazon.es/Xiaomi-Puls%C3%B3metro-sofortnachr-Resistente-meteorol%C3%B3gica/dp/B07DG3P996"
#response = requests.get(url)
#soup = BeautifulSoup(response.text, "html.parser")
#name = soup.find("span", {"id": "productTitle"}).text.lstrip().rstrip()
#price = soup.find("span", {"id": "priceblock_ourprice"}).text
#price = price.replace(",", ".")
#tamano = len(price)
#price = price[4:tamano]

#print(float(price), name)

client = MongoClient(mongo)

db = client.test

collection = db.producto

producto = collection.find_one()

collection.update_one({"id_usuario":287238671, "nombre":"Voopoo Drag 2 Starter kit, Cigarrillo Electrónico Kit Vapor eCig Chips FIT-Modo 177W Box Mod Atomizador Uforce T2 Tank 5ml - Sin Nicotina y Sin E-líquido (B-scarlet)"}, { "$set": {"precio": 30.0}})

print("Precio de amazon: " + str(producto["precio"]) + " y el precio de la url es: " + str(obtenerPrecio(producto["url"])))

#print(id)

#ejem1 = collection.find_one({"name":name})
#print(ejem1["name"])

