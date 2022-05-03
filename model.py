import json
import datetime

class Product():
    def __init__(self, name, description = "", manufacturer = "", weight = "") -> None:
        self.name = name
        self.description = description
        self.company = manufacturer
        self.weight = weight

class ProductCard(Product):
    def __init__(self, attrs={}, image="", site=""):
        self.attrs = attrs
        self.image = image
        self.site = site
    
    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)
    
        