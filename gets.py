import requests
from bs4 import BeautifulSoup

def obtenerNombre(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    name = soup.find("span", {"id": "productTitle"}).text.lstrip().rstrip()
    return name

def obtenerPrecio(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    price = soup.find("span", {"id": "priceblock_ourprice"}).text
    price = price.replace(",", ".")
    tamano = len(price)
    price = price[4:tamano]
    return price