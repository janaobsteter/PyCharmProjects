from modules.database import Database

class Price(object):
    def __init__(self, productName, specs, price):
        self.name = productName
        self.spec = specs
        self.price = price

    def displayPrice(self):
        return self.price

    def json(self):
        return {
            "Product Name": self.name,
            "Specification": self.spec,
            "Price": self.price
        }

    def save_to_db(self, collection):
        Database.insert(collection=collection,
                        data=self.json())