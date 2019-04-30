import uuid
from database import Database
import datetime


class Post(object):
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        # self.id = id
        self.id = uuid.uuid4().hex if id is None else id
        #uuid = universly unique identifier, uiid4 generates id, #4 is random id, .hex = 32bit character hexadecimal string
        self.date = date

    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.json()) #import into database into posts collection

    def json(self): #creates a json representation of the post
        return {
            "id": self.id,
            "blog_id": self.blog_id,
            "date": self.date,
            "title": self.title,
            "author": self.author,
            "content": self.content
        }

    @classmethod
    def from_mongo(cls, id): #Post.from_mongo(posdID) returns the post from mongo
       post_data = Database.find_one(collection="posts", query={"id": id})
       return cls(blog_id=post_data["blog_id"],
                  title=post_data["title"],
                  content=post_data["content"],
                  author=post_data["author"],
                  date=post_data["date"],
                  id=post_data["id"])

    @staticmethod
    #return all posts belonging to a blog
    def from_blog(blog_id):
        # return "\n".join(map(str, [post for post in Database.find(collection="blogs",
        #                                                           query={"blog_id": blogid})])) #find returns cursor
        return [post for post in Database.find(collection="posts",
                                               query={"blog_id": blog_id})] #find returns cursor

