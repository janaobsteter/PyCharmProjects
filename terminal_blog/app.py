import pymongo

#127.0.0.1 is always the local machine

uri = "mongodb://127.0.0.1:27017" #server:port
#initialise mongodb client - that has access to all db on your computer
client = pymongo.MongoClient(uri)
database = client['webdeveloping']
collection = database['students']
#
#
# #students = collection.find({})
#
# print([student for student in collection.find({}) if student['Ocena'] > 50])#shift + F6 to rename variable

from modules.post import Post

post = Post(897348723, "Sunday", "Icecream day", "Jana", "28-09-2018", 897)
post.json()
 




