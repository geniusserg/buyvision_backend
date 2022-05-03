from email import parser
from bs4 import BeautifulSoup
import requests 
from model import Product


class Parser():
    def parse(html):
        pass

class ParserGS1(Parser):
    def parse(self,html):
        bs = BeautifulSoup(html, 'html.parser')
        try:
            name = bs.select('body > div > div.content-wrap--shadow > section > div.product-card__header-block > p.product-card__header-product-name')[0].string.strip()
        except IndexError:
            return None
        company = bs.select('body > div > div.content-wrap--shadow > section > div.product-card__header-block > p.product-card__header-company')[0].string.strip()
        brand = bs.find_all('table', recursive=True)[1].find_all('tr', recursive=True)[2].find('span', attrs={'class':'text2'}).text.strip()
        weight = bs.find_all('table', recursive=True)[1].find_all('tr', recursive=True)[3].find('span', attrs={'class':'text2'}).text.strip()
        return Product(brand, name, company, weight) # gtin is separatly defined

class ParserBL(Parser):
    def parse(self,html):
        pass


urls = {
    'gs1': "https://srs.gs1ru.org/id/gtin/",  
    'bl' : "https://barcode-list.ru/barcode/RU/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA.htm?barcode="
}

parsers = {
    'gs1': ParserGS1(),
    'bl' : ParserBL()
}

def getProducts(gtin, method="gs1"):
    htmlOutput = requests.get(urls[method]+gtin).text
    print(urls[method]+gtin)
    result =  parsers[method].parse(htmlOutput)
    return result

getProducts("4607092074702")
