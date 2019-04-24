from pymongo import MongoClient
from private import mongo
import requests
from bs4 import BeautifulSoup

def insert(id, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    name = soup.find("span", {"id": "productTitle"}).text.lstrip().rstrip()
    price = soup.find("span", {"id": "priceblock_ourprice"}).text

    client = MongoClient(mongo)
    db = client.test
    collection = db.producto
    consulta = {"id_usuario": id, "nombre": name, "precio": price, "url": url}
    collection.insert_one(consulta)