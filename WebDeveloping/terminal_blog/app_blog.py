from database import Database
from modules.blog import Blog


Database.initialise() #this created Database.DATABASE


#what do we want to do with a blog?
blog = Blog(author = "Jana",
            title = "Blog title",
            description = "Sample description")

print("This is new post")
#saves a post to mongodb
blog.new_post()

print("This is save")
#saves the blog to mongodb
blog.save_to_mongo()

print("this is the from_mongo")
#get the blog from the db - this returns a Blog objecz
from_db = Blog.from_mongo(blog.blog_id)

print("these are the posts")
#print(blog.get_posts())
print(from_db.get_posts())
