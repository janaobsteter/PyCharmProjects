from passlib.hash import pbkdf2_sha512

class Utils(object):

    @staticmethod
    def hash_password(password):
        """
        Hashes a password using pbkdf2_sha512
        :param password: Tha sha_512 passord from the Login/Register
        :return: a sha_512 > pbkdf2_sha512 encrypted password
        """
        return pbkdf2_sha512.encrypt(password)


    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        Checks that the password user sent matches that of the database
        The database password in encrypted more than the user password at this stage
        :param password: sha512-hashed password
        :param hashed_password: database password - pbkdf2_sha512 encrypted password
        :return: True if passwords match and False otherwise
        """
        return pbkdf2_sha512.verify(password, hashed_password)