from modules.post import Post
from database import Database
import uuid
import datetime

class Blog(object):
    def __init__(self, author, title, description, blog_id = None):
        self.author = author
        self.title = title
        self.description = description
        self.blog_id = uuid.uuid4().hex if blog_id is None else blog_id

    def new_post(self):
        content = input("Enter post content: ")
        title = input("Enter post title: ")
        date = input("Enter post date or leve blank for today [DDMMYY]: ")
        if not date:
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%y")

        post = Post(blog_id = self.blog_id,
                    author = self.author,
                    title = title,
                    content = content,
                    date=date)
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.blog_id)

    def save_to_mongo(self): #this saves the blog to mongo
        Database.insert(collection="blogs", data=self.json())

    def json(self):
        return {
            "blog_id": self.blog_id,
            "author": self.author,
            "title": self.title,
            "description": self.description}

    #this is with static method, which is a bit cumbersome
    # @staticmethod
    # def get_from_mongo(blog_id): #here we are getting the blog, so we do not have an instance yet
    #     blog_data = Database.find_one(collection = "blogs",
    #                       query={"blog_id": blog_id}) #but if we return only data, we wont be able to call the methods
    #     #onto the blog - like get posts etc.
    #     return Blog(author = blog_data["author"],
    #                 title = blog_data["title"],
    #                 description = blog_data["description"],
    #                 blog_id = blog_id)

    #this is with class method
    @classmethod
    def from_mongo(cls, blog_id): #here we are getting the blog, so we do not have an instance yet
        blog_data = Database.find_one(collection = "blogs",
                          query={"blog_id": blog_id}) #but if we return only data, we wont be able to call the methods
        #onto the blog - like get posts etc.
        return cls(author = blog_data["author"],
                    title = blog_data["title"],
                    description = blog_data["description"],
                    blog_id = blog_data["blog_id"])

#blog = Blog(uuid.uuid4().hex, "Jana")
#print(blog.new_post(title="BlogDay", data="This is creating a blog"))
