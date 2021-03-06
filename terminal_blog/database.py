import pymongo

class Database(object): #if you specify object, it inherits from the object - all the methods
    #this does not go into self, because we want them all to have the same URI and DATABASE
    URI = "mongodb://127.0.0.1:27017" #universal resource identifier, it its going to be mongo identifier
    DATABASE = None

    #it is a static method do it can be used by many files without creating many instance
    #each instance connect by itself to the database which is slow and unefficient
    @staticmethod #because this method belongs to the database class as a whole and not only to one isntance
    def initialise():
        client = pymongo.MongoClient(Database.URI) #since URI is not defined in the method, you have to specify that it lives in the Database
        Database.DATABASE = client['webdeveloping']


    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)


    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)


    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

