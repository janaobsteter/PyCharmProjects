<<<<<<< Updated upstream
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> a960e91a7e7f979d8e86921c1c861db15f8a5d79
=======
>>>>>>> Stashed changes

__author__ = "janao"

import pymongo

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialise(database):
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client[database]

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

<<<<<<< Updated upstream
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD


=======
>>>>>>> a960e91a7e7f979d8e86921c1c861db15f8a5d79
=======
>>>>>>> a960e91a7e7f979d8e86921c1c861db15f8a5d79
=======
>>>>>>> a960e91a7e7f979d8e86921c1c861db15f8a5d79
=======
>>>>>>> a960e91a7e7f979d8e86921c1c861db15f8a5d79
>>>>>>> Stashed changes
