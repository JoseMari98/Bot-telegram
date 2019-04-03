import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from pymongo import MongoClient
from private import mongo

url = "https://www.amazon.es/Xiaomi-Puls%C3%B3metro-sofortnachr-Resistente-meteorol%C3%B3gica/dp/B07DG3P996?pd_rd_wg=y3DHX&pd_rd_r=aa03e607-b352-417a-96d2-c16857d48a56&pd_rd_w=ozFrQ&ref_=pd_gw_ri&pf_rd_r=EM0163T4D7HX8N4KDKT3&pf_rd_p=3187c5a7-b24d-5d8f-ba5a-bd70f4f3b001"
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

ejem1 = collection.find({"name":name})
for doc in ejem1:
    print(doc)