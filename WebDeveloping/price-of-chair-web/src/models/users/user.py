import uuid

from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors
from src.models.alerts.alert import Alert


class User(object):
    def __init__(self,  email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if not _id else _id

    def __repr__(self):
        return "<User {}.".format(self.email)

    @staticmethod #static method - because we are not talking a specific user, but a password and useremail
    #we do not yet have a user
    def is_login_valid(user_email, password):
        """
        This method verifies that as email - password combo (send by this site forms) is valid
        Checks that email exists and that password associated with this email is correst
        :param user_email: The user's email, string
        :param password: hashed passowrd sha512
        :return: True if valid, False otherwise
        """
        user_data = Database.find_one('users', {'email': user_email}) #password in sha512 --> pbkdf2_sha512 (in the database)
        if not user_data:
            #Tell the user that their email doe not exist
            raise UserErrors.UserNotExistsError("Your user does not exist")

        if not Utils.check_hashed_password(password, user_data['password']):
            raise UserErrors.IncorrectPasswordError("The password is incorrect")

        return True

    @staticmethod
    def register_user(email, password):
        """
        This method registers a user with an email and password
        The password already comes hashed as sha512
        :param email: user email, which might be invalid
        :param password:sha512-hashed password
        :return: True if registration successful, otherwise False (excpetions might be raised)
        """

        user_data = Database.find_one('users', {"email": email})
        if user_data:
            #tell user they are already registered"
            raise UserErrors.UserAlreadyRegistered("The email you provided is already registered.")

        if not Utils.email_is_valid:
            #tell the user the email is not constructed properly
            raise UserErrors.InvalidEmailError("The format of the email is not correct.")

        User(email, Utils.hash_password(password)).save_to_db()

        return True

    def save_to_db(self):
        Database.insert("users", self.json())

    def json(self):
        return {
            "email": self.email,
            "password": self.password,
            "_id": self._id
        }

    @classmethod
    def find_by_email(cls, email):
        return cls(**Database.find_one('users', {'email': email}))

    def get_alerts(self): #now the module can deal with another module - they are at the same level
        #but you do not want one views to deal with two modules
        return Alert.find_by_user_email(self.email)




