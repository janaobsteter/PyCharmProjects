import uuid

import requests
from bs4 import BeautifulSoup
import re

from src.common.database import Database
import src.models.items.constants as ItemConstants


class Item(object):
    def __init__(self, name, url, store, _id=None):
        self._id = uuid.uuid4().hex if not _id else _id
        self.name = name
        self.url = url
        tag_name = store.tag_name
        query = store.query
        self.price = self.load_price(tag_name, query)

    def __repr__(self):
        return "<Item {} with URL {}.".format(self.name, self.url)

    def load_price(self, tag_name, query):
        request = requests.get(self.url)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(tag_name, query)
        string_price = element.text.strip()
        pattern = re.compile("(\d+.\d+)") # for $115.00, the brackets are there to EXTRACT the matching pattern - without it
        #it just tels you whether it is there or not
        match = pattern.search(string_price)

        return match.group() #get the ifrst group that matches

    def save_to_db(self):
        Database.insert(ItemConstants.COLLECTION, self.json)

    @classmethod
    def from_db(cls, name):
        item_data = Database.find_one(ItemConstants.COLLECTION, {"name": name})
        return cls(**item_data)

    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "url": self.url,
            "price": self.price
        }



