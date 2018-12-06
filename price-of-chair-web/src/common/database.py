import pymongo

class Database(object):
    def __init__(self):
        URI = "mongodb://127.0.0.1:27017"
        DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['webdeveloping']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE.insert(collection, data)

    @staticmethod
    def find(collection, query):
        Database.DATABASE.find(collection, query)

    @staticmethod
    def find_one(collection, query):
        Database.DATABASE.find_one(collection, query)