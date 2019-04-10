import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from pymongo import MongoClient
from private import mongo

url = "https://www.amazon.es/Xiaomi-Puls%C3%B3metro-sofortnachr-Resistente-meteorol%C3%B3gica/dp/B07DG3P996"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
name = soup.find("span", {"id": "productTitle"}).text.lstrip().rstrip()
price = soup.find("span", {"id": "priceblock_ourprice"}).text


print(price, name)

client = MongoClient(mongo)

db = client.test

collection = db.test

ejem = {"name":name,"price":price}
id = collection.insert_one(ejem).inserted_id

print(id)

ejem1 = collection.find_one({"name":name})
print(ejem1["name"])

