from bs4 import BeautifulSoup
import requests
import model 
from model import ProductCard

class ParserLenta():
    def parse(self,html):
        bs = BeautifulSoup(html, 'html.parser')
        attrs = {}
        for item in bs.find_all('div', attrs={"class": "sku-card-tab-params__item"}):
            attr = item.find('label', attrs={"class": "sku-card-tab-params__label"}).text
            val = item.find('label', attrs={"class": "sku-card-tab-params__value"}).text
            attrs[attr] = val
        image = bs.find_all('sku-images-slider__current-image js-sku-images-slider-image')[0]['href']
        return ProductCard(attrs, image=image, site="lenta.ru")

def getProductCard(productUrl):
    htmlOutput = requests.get(productUrl).text
    result =  ParserLenta().parse(htmlOutput)
    return result

print(getProductCard("https://lenta.com/product/maslo-podsolnechnoe-miladora-raf-dez-vymorozh-1-sort-rossiya-09l-585662/"))