from flask import Flask, render_template, request, session

#use Flask to define app
#creating Flask application
from src.common.database import Database
from src.modules.user import User

app = Flask(__name__) # '__main__'
#we have to add the secret key - to make sure that the cookie we are sending is secure
app.secret_key = "janao"


#create API endpoints
@app.route('/')
def home_template():
    return render_template('home.html')

@app.route('/login') #www.mysite.com/api/
def login_template():
    return render_template('login.html')# flask nows that this lives in the template folder

@app.route('/register') #www.mysite.com/api/
def register_template():
    return render_template('register.html')# flask nows that this lives in the template folder

@app.before_first_request #IT will run the method before the first request
def initialise_database():
    Database.initialise("webdeveloping")


@app.route('/auth/login', methods = ['POST']) #we are accepting only post requests
def login_user():
    email = request.form['email']
    password = request.form['password']
    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None
    return render_template("profile.html", email = session['email'])


@app.route('/auth/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']
    User.register(email, password)
    return render_template("profile.html", email = session['email'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)
