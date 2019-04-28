#to allow users to log in and create pblogs ...
import uuid

import datetime
from flask import session

from src.common.database import Database
from src.modules.blog import Blog


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    #this is a class methods because when we are passing in the user we do not already have the user
    @classmethod
    def get_by_email(cls, email): #get_from_mongo - get the USER
        data = Database.find_one("users", {"email": email}) #collection is users
        if data:
            return cls(**data)

    @classmethod #is the user does not exist, this does nothing
    def get_by_id(cls, _id):
        data = Database.find_one("users", {"_id": _id})
        if data:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        #whether the users email matches the password
        user = User.get_by_email(email)
        if user: #if the user exists, check the password
            return user.password == password
        return False

    @classmethod #this is a class method only for when we change user class name, we do not have to change the name here as well
    def register(cls, email, password):
        #check whether the user exists
        user = User.get_by_email(email)
        if not user:
            new_user = cls(email, password)
            new_user.save_to_mongo()
            session["email"] = email #so that the user is logged in when it registers
            #flask does the cookies for us - it knows that the user's cookie matches this session
            return True #better than to return None
        else:
            print("Registration failed.")
            return False

    @staticmethod
    def login(user_email):
        #login_valid has already been called - we now that the user has a valid email and password
        #store their email in the session
        #next time the user logs in they send us a unique identifier in their cookie
        #this cookie identifies this session and the session gfives the email
        #if the session does not have an email, it mean that the user has not yet logged in
        session["email"] = user_email #the only thing we need to do is to store their email
        #this is to match the cookie and the session

    @staticmethod
    def logout():
        session["email"] = None

    def new_blog(self, title, description):
        blog = Blog(author=self.email,
                    author_id = self._id,
                    title=title,
                    description=description)
        blog.save_to_mongo()

    @staticmethod
    def new_post( blog_id, title, content, date=datetime.datetime.utcnow()):
        #the website will send us the  blog_id, when the user presses submit
        blog = Blog.from_mongo(blog_id)
        blog.new_post(title, content, date)

    def get_blogs(self):
        return Blog.find_by_author_id(self._id)

    def save_to_mongo(self):
        Database.insert("users", self.json())

    def json(self):
        return {
            "email": self.email,
            "_id": self._id,
            "password": self.password #IF we are using this method to communicate with the user, it is not safe to put the password in here
            #if we are going to use this method only within app, than its ok
            #you should NOT SEND THIS OVER THE NETWORK
        }


    #session is the same as cookie, but on the server side.
    #cookie is on the browser site