import id_url
import requests
from bs4 import BeautifulSoup

objetoIdUrl =
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
name = soup.find("span", {"id": "productTitle"}).text.lstrip().rstrip()
price = soup.find("span", {"id": "priceblock_ourprice"}).text


print(price, name)