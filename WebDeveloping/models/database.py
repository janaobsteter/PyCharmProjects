import pymongo

class Database(object):
    URI = "mongodb://127.0.0.1:27017"  #universal resource indentifier
    DATABASE = None

    @staticmethod
    def initialise():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client["webdeveloping"]

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        Database.DATABASE[collection].find(query) #returns the cursor(start at the first element, go through all)

    @staticmethod
    def find_one(collection, query):
        Database.DATABASE[collection].find_one(query) #gets the first element returned by the cursor