class Post(object):
    def __init__(self, blogID,title, content, author, date, id):
        self.blogID = blogID
        self.title = title
        self.content = content
        self.author = author
        self.id = id
        self.date = date

    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.json) #import into database into posts collection

    def json(self): #creates a json representation of the post
        return {
            "id": self.id,
            "blog_id": self.blogID,
            "date": self.date,
            "title": self.title,
            "author": self.author,
            "content": self.content
        }

