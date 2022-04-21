import json
import datetime

class GTINAnswer():
    def __init__(self, gtin, product=None, status="Success"):
        self.date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.gtin = gtin
        self.product = product
        self.status = status

class Product():
    def __init__(self, name, brand = "", company = "", weight = "") -> None:
        self.name = name
        self.brand = brand
        self.company = company
        self.weight = weight

class ProductCard(Product):
    def __init__(self, attrs={}, image="", site=""):
        self.attrs = attrs
        self.image = image
        self.site = site
        