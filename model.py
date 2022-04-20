import json
class Product():
    gtin = ""
    name = ""
    brand = ""
    company = ""
    weight = ""
    
    def __init__(self, gtin, name, brand = "", company = "", weight = "") -> None:
        self.gtin = gtin
        self.name = name
        self.brand = brand
        self.company = company
        self.weight = weight
    
    def toJson(self):
        return json.dump(self.__dict__)