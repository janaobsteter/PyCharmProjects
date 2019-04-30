#import pymongo
from database import Database
#from modules.blog import Blog
from modules.post import Post

#127.0.0.1 is always the local machine

# uri = "mongodb://127.0.0.1:27017" #server:port
# #initialise mongodb client - that has access to all db on your computer
# client = pymongo.MongoClient(uri)
# database = client['webdeveloping']
# collection = database['students']
# #
# #
# # #students = collection.find({})
# #
# # print([student for student in collection.find({}) if student['Ocena'] > 50])#shift + F6 to rename variable
#
# from modules.post import Post
# from database import *
#
#
# #first we have to initialise connection to the data
Database.initialise() #this created Database.DATABASE

# post = Post(897348723, "Sunday", "Icecream day", "Jana", "28-09-2018", 897)
# post.json()

# post = Post(blogID="123",
#             title="New post",
#             content="This is our first post",
#             author="Jana")
#
# post2 = Post(blogID="123",
#             title="Second post",
#             content="This is our second post",
#             author="Jana")

#print(post.json())
#post2.save_to_mongo()

#print(Post.from_mongo("11bcf2530f3643fd9f41c3d248cf8445"))
# print(Post.from_blog("123"))


#what do we want to do with a blog?
blog = Blog(author = "Jose",
            title = "Blog title",
            description = "Sample description")

blog.new_post()

blog.save_to_mongo()

Blog.from_mongo()

blog.get_posts()





