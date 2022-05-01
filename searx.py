import requests
import json 
import time
from lenta import getProductCard

searx_url = "https://searx.tyil.nl/search?q={query}&categories=images&language=ru-RU&format=json"

known_urls = ["www.auchan.ru", "perekrestok", "lenta.com", "market.yandex.com", "sbermarket.ru", "market.yandex.ru", "myspar.ru", "www.ozon.ru", "otzovik.com", "www.youtube.com", "www.eapteka.ru"]

def search(query):
    js = requests.get(searx_url.replace("{query}", query)).text
    if "Rate limit exceeded" in js:
        print("Warning: rate limit exceeded, need to wait...")
        time.sleep(20)
        js = requests.get(searx_url.replace("{query}", query)).text
    return [i['url'] for i in json.loads(js)['results'] if i['parsed_url'][1] in known_urls]

def sttt(js):
    return "{ \"results\" : [\""+"\", \"".join([ i['url'] for i in json.loads(js)['results'] if i['parsed_url'][1] in known_urls])+"\"]}"

res = search("Бедро куриное Петелинка в маринаде Барбекю охлажденное")

print(res)

for i in res:
    if "lenta.com" in i:
        print(" \n ---LENTA:--- \n"+json.dumps(getProductCard(i).__dict__, ensure_ascii=False))


