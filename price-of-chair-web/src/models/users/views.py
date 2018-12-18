from flask import Blueprint, request, session, redirect, url_for, render_template

#view is the endpoint of the API
from src.models.users.user import User
import src.models.users.errors as UserErrors

user_blueprint = Blueprint('users', __name__) #__name__ is the name of the file while it is running
#you can give it template folder if it is not 'templates'

@user_blueprint.route('/login', methods=['POST', 'GET']) #if the method is get - give them the login form, is POST - send us useremail and password
def login_user():
    if request.method == "POST":
        #check login is valid
        email = request.form['email']
        password = request.form['hashed']
        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return redirect(url_for(".user_alerts")) #url_for gets a methods for the current method - which is this file
        except Exception as e:
            return e.message
    return render_template("users/login.html") #improvements: send the user and error if their login was invladi

@user_blueprint.route('/register', methods=['GET', 'POST'])

def register_user():
    if request.method == "POST":
        #check login is valid
        email = request.form['email']
        password = request.form['hashed']
        try:
            if User.register_user(email, password):
                session['email'] = email
                return redirect(url_for(".user_alerts")) #url_for gets a methods for the current method - which is this file
        except UserErrors.UserError as e:
            return e.message
    return render_template("users/register.html") #improvements: send the user and error if their login was invladi

@user_blueprint.route('/alerts')
def user_alerts():
    return "This is an alert page"

@user_blueprint.route('/logout')
def logout():
    pass

@user_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alerts():
    pass



