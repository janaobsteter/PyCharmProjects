from database import Database
from modules.blog import Blog


class Menu(object):
    def __init__(self):
        # askt he user for authors name
        self.user = input("Enter name: ")
        self.user_blog = None
        # check if user has an account
        if self._user_has_account():  # _ before the method tells us that this methods are only to be used within the class (PRIVATE!)
            # they can be called from other python files, but should not be
            print("Welcome back, {}!".format(self.user))
        # if not, prompt to crate one
        else:
            print("You do not have an account! Creating the blog ...")
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one(collection="blogs", query={"author": self.user})
        if blog:
            self.user_blog = Blog.from_mongo(blog_id=blog["blog_id"])
            return True
        else:
            return False

    def _prompt_user_for_account(self):  # basically start a blog
        title = input("Enter blog title: ")
        description = input("Describe the blog: ")
        blog = Blog(author=self.user, title=title, description=description)
        blog.save_to_mongo()
        print("Congratulation, {}! You've created a blog!".format(self.user))
        self.user_blog = blog  # the created blog is now users blog

    def run_menu(self):  # gives the use the choice to write/read blogs ...
        # user read or write blogs
        read_write = input("Do you want to read (r) or write the blog (w) or terminate (T)?")
        if read_write == "r":
            # list blogs in database
            self._list_blogs()
            # allow user to choose one
            # display posts
            self._view_blog()
        elif read_write == "w":
            # check if user has a blog - if they want to write, they have a blog
            # prompt to write a post - but you need blogID for this
            self.user_blog.new_post()
        elif read_write == "T":
            print("Bye bye.")
            exit

        # else:
        #     print("Unexpected character!")

    def _list_blogs(self):
        blogs = Database.find(collection="blogs",
                              query={})
        print("\n".join(
            ["ID: {}, Title: {}, Author: {}".format(blog["blog_id"], blog["title"], blog["author"]) for blog in blogs]))

    def _view_blog(self):
        #blog_id = input("Enter the chosen blog_id: ")
        field = input("Do you want to seach by author (a), title (t) or blog id (i)? ")
        if field == "a":
            author = input("Enter the author: ")
            blog_id = Database.find_one(collection="blogs", query={"author": author})["blog_id"]
        if field == "t":
            title = input("Enter the title: ")
            blog_id = Database.find_one(collection="blogs", query={"title": title})["blog_id"]
        if field == "i":
            blog_id = input("Enter the id: ")
        blog = Blog.from_mongo(blog_id)
        for _post in blog.get_posts():
            print("Date: {}, title: {}\n\n{}".format(_post["date"], _post["title"], _post["content"]))
        # except:
        #     print("No content. Pick another blog_id")
        #     self._view_blog()