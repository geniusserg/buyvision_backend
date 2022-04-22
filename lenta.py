from bs4 import BeautifulSoup
import requests
import model 
from model import ProductCard

class ParserLenta():
    def parse(self,html):
        bs = BeautifulSoup(html, 'lxml')
        attrs = {}
        for item in bs.find_all(class_="sku-card-tab-params__item"):
            attr = item.find(class_= "sku-card-tab-params__label").text
            val = item.find("meta")['content']
            attrs[attr] = val
        image = bs.find(class_='sku-images-slider__current-image js-sku-images-slider-image')
        if image != None:
            image = image['src']
        return ProductCard(attrs, image=image, site="lenta.ru")

def getProductCard(productUrl):
    htmlOutput = requests.get(productUrl, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}).text
    result =  ParserLenta().parse(htmlOutput)
    return result
