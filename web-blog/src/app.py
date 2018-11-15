from flask import Flask, render_template, request, session

#use Flask to define app
#creating Flask application
from src.modules.user import User

app = Flask(__name__) # '__main__'


#create API endpoints
@app.route('/') #www.mysite.com/api/
def hello_method():
    return render_template('login.html')# flask nows that this lives in the template folder

@app.route('/login')
def login_user():
    email = request.form(['email'])
    password = request.form(['password'])
    if User.login_valid(email, password):
        User.login(email)
    return render_template("profile.html", email = session['email'])




if __name__ == '__main__':
    app.run(port=5000, debug=True)
