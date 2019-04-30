import uuid
from src.common.database import Database
import datetime


class Post(object):
<<<<<<< Updated upstream
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow()):
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), _id=None):
=======
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow()):
>>>>>>> a960e91a7e7f979d8e86921c1c861db15f8a5d79
=======
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow()):
>>>>>>> a960e91a7e7f979d8e86921c1c861db15f8a5d79
=======
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow()):
>>>>>>> a960e91a7e7f979d8e86921c1c861db15f8a5d79
=======
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow()):
>>>>>>> a960e91a7e7f979d8e86921c1c861db15f8a5d79
>>>>>>> Stashed changes
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        # self.id = id
<<<<<<< Updated upstream
        self._id = uuid.uuid4().hex if blog_id is None else blog_id
        #uuid = universly unique identifier, uiid4 generates id, #4 is random id, .hex = 32bit character hexadecimal $
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        self._id = uuid.uuid4().hex if _id is None else _id
        #uuid = universly unique identifier, uiid4 generates id, #4 is random id, .hex = 32bit character hexadecimal string
=======
        self._id = uuid.uuid4().hex if blog_id is None else blog_id
        #uuid = universly unique identifier, uiid4 generates id, #4 is random id, .hex = 32bit character hexadecimal $
>>>>>>> a960e91a7e7f979d8e86921c1c861db15f8a5d79
=======
        self._id = uuid.uuid4().hex if blog_id is None else blog_id
        #uuid = universly unique identifier, uiid4 generates id, #4 is random id, .hex = 32bit character hexadecimal $
>>>>>>> a960e91a7e7f979d8e86921c1c861db15f8a5d79
=======
        self._id = uuid.uuid4().hex if blog_id is None else blog_id
        #uuid = universly unique identifier, uiid4 generates id, #4 is random id, .hex = 32bit character hexadecimal $
>>>>>>> a960e91a7e7f979d8e86921c1c861db15f8a5d79
=======
        self._id = uuid.uuid4().hex if blog_id is None else blog_id
        #uuid = universly unique identifier, uiid4 generates id, #4 is random id, .hex = 32bit character hexadecimal $
>>>>>>> a960e91a7e7f979d8e86921c1c861db15f8a5d79
>>>>>>> Stashed changes
        self.date = date

    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.json()) #import into database into posts collection

    def json(self): #creates a json representation of the post
        return {
            "_id": self._id,
            "blog_id": self.blog_id,
            "date": self.date,
            "title": self.title,
            "author": self.author,
            "content": self.content
        }

    @classmethod
    def from_mongo(cls, id): #Post.from_mongo(posdID) returns the post from mongo
       post_data = Database.find_one(collection="posts", query={"_id": id})
       return cls(**post_data)

    @staticmethod
    #return all posts belonging to a blog
    def from_blog(blog_id):
        # return "\n".join(map(str, [post for post in Database.find(collection="blogs",
        #                                                           query={"blog_id": blogid})])) #find returns cursor
        return [post for post in Database.find(collection="posts",
                                               query={"blog_id": blog_id})] #find returns cursor
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
