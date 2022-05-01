from bs4 import BeautifulSoup
import requests
import model 
from model import ProductCard

class ParserAuchan():
    def parse(self,html):
        bs = BeautifulSoup(html, 'lxml')
        attrs = {}
        price = bs.find_all(class_="css-avjdfx").text

        
        return ProductCard(attrs, image=image, site="auchan.ru")

def getProductCard(productUrl):
    htmlOutput = requests.get(productUrl, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}).text
    result =  ParserAuchan().parse(htmlOutput)
    return result

