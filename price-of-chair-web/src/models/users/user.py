import uuid

from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors


class User(object):
    def __init__(self, name, email, password, _id=None):
        self.name = name
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




