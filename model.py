import json
import datetime

class GTINAnswer():
    gtin = ""
    products = []
    status = ""
    date = ""
    def __init__(self, gtin, products=[], status="Success"):
        self.date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.gtin = gtin
        self.products = products
        self.status = status

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
    