import uuid

from src.common.database import Database
import src.models.stores.constants as StoreConstants


class Store(object):
    def __init__(self, name, url_prefix, tag_name, query, _id=None):
        self.name = name
        self.url_prefix = url_prefix
        self.tag_name = tag_name
        self.query = query
        self._id = uuid.uuid4().hex if not _id else _id

    def __repr__(self):
        return "<Store {} with url prefix {}.".format(self.name, self.url_prefix)

    def json(self):
        return {
            "name": self.name,
            "url_prefix": self.url_prefix,
            "tag_name": self.tag_name,
            "query": self.query,
            "_id": self._id
        }

    @classmethod
    def get_by_id(cls, id):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"_id": id}))

    def save_to_db(self):
        Database.insert(StoreConstants.COLLECTION, self.json())

    @classmethod
    def get_by_name(cls, store_name):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"name": store_name}))

    @classmethod
    def get_by_url_prefix(cls, url_prefix):
        """
        http://www.amazon -->http://www.amazon.com
        This allows us to search - whether the two strings belong the same way
        if they give us http://www.amaz -- > http://www.amazon.com
        h --> matches anything?
        ht -->
        htt -->


        http://www.amazon --> Store object
        :param url_prefix:
        :return:
        """
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"url_prefix": {"$regex": '^{}'.format(url_prefix)}}))

    @classmethod
    def find_by_url(cls, url):
        """
        return a store from a url like http://www.amazon.com/item/987327324.html
        we are going to find a store from an items url
        :param url: item's URL
        :return: a store if found, error if not
        """
        for i in
        return cls(**Database.find)