import uuid



import requests
from bs4 import BeautifulSoup
import re

from src.common.database import Database
import src.models.items.constants as ItemConstants
from src.models.stores.store import Store


class Item(object):
    def __init__(self, name, url, _id=None):
        self._id = uuid.uuid4().hex if not _id else _id
        self.name = name
        self.url = url
        store = Store.find_by_url(url)
        #self.store_name = store.name
        self.tag_name = store.tag_name
        self.query = store.query
        self.price = None

    def __repr__(self):
        return "<Item {} with URL {}.".format(self.name, self.url)

    def load_price(self):
        request = requests.get(self.url)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        #print(soup)
        #print(self.tag_name, self.query)
        element = soup.find(self.tag_name, self.query)
        string_price = element.text.strip()

        pattern = re.compile("(\d+.\d+)") # for $115.00, the brackets are there to EXTRACT the matching pattern - without it
        #it just tels you whether it is there or not
        match = pattern.search(string_price)

        self.price = float(match.group())
        return self.price #get the ifrst group that matches, we are updating the price!

    def save_to_db(self):
        Database.insert(ItemConstants.COLLECTION, self.json)

    @classmethod
    def from_db(cls, name):
        item_data = Database.find_one(ItemConstants.COLLECTION, {"name": name})
        return cls(**item_data)

    @classmethod
    def get_by_id(cls, _id):
        return cls(**Database.find_one(ItemConstants.COLLECTION, {"_id": _id}))

    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "url": self.url,
            "price": self.price
        }



