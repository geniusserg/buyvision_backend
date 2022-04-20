import json
import datetime

class GTINAnswer():
    gtin = ""
    products = []
    error = ""
    date = ""
    def __init__(self, gtin, products=[], error=""):
        self.date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.gtin = gtin
        self.products = products

class Product():
    description = ""
    brand = ""
    company = ""
    weight = ""
    
    def __init__(self, name, brand = "", company = "", weight = "") -> None:
        self.name = name
        self.brand = brand
        self.company = company
        self.weight = weight
    