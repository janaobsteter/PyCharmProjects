class Post(object):

    def __init__(self, blogid, title, content, author, date, id):
        self.blogid = blogid
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.id = id

    def save_to_mongo(self):
        Database.insert(collection = "posts", data = self.json())

    def json(self):
        return {
            "id": self.id,
            "blogid": self.blogid,
            "author": self.author,
            "content": self.content,
            "title": self.title,
            "created_date": self.date
        }


    @staticmethod
    def from_mongo(id): #returns the mongo data based on the id
         return Database.find_one(collection="posts", query={"id":id})

    @staticmethod
    def from_blog(blogid):
        return [post for post in Database.find(collection="posts", query={"blogid": blogid})] #finds all of the posts, returns CUROSR!!!

    
