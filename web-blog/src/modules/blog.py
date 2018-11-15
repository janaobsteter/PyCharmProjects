from src.modules.post import Post
from src.common.database import Database
import uuid
import datetime

#there are some things that need improving
#1) blog_id is not the same ID as the mongodb gives to the objects
#mongodb gives each document _id - we should overwrite mongodb ID with our ID
#so rename blog_id with _id
#because we use API we dont ahve to worry about changing it in other apps

#2) change imports from src. ...

#3) simplify cls

#4) change the inputs since thy will be coming from the browser

class Blog(object):
    def __init__(self, author, author_id, title, description, blog_id = None):
        self.author = author
        self.author_id = author_id
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if blog_id is None else blog_id

    def new_post(self, title, content, date=datetime.datetime.utcnow()):
        post = Post(blog_id= self._id,
                    author = self.author,
                    title = title,
                    content = content,
                    date=date) #is the user does not specify a date, then use now
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self): #this saves the blog to mongo
        Database.insert(collection="blogs", data=self.json())

    def json(self):
        return {
            "_id": self._id,
            "author": self.author,
            "author_id": self.author_id,
            "title": self.title,
            "description": self.description}

    @classmethod
    def from_mongo(cls, _id): #here we are getting the blog, so we do not have an instance yet
        blog_data = Database.find_one(collection = "blogs",
                          query={"_id": _id}) #but if we return only data, we wont be able to call the methods
        #onto the blog - like get posts etc.
        return cls(**blog_data)

    @classmethod
    def find_by_author_id(cls, author_id):
        return [cls(blog) for blog in  Database.find(collection="blogs", query={"author_id": author_id})]
    #this is returning list of Blog objects
