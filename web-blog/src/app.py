from flask import Flask, render_template, request, session

#use Flask to define app
#creating Flask application
from src.common.database import Database
from src.modules.blog import Blog
from src.modules.user import User

app = Flask(__name__) # '__main__'
app.secret_key = "janao"

#create API endpoints
@app.route('/') #www.mysite.com/api/
def home_template():
    return render_template('home.html')# flask nows that this lives in the template folder

@app.route('/login') #www.mysite.com/api/
def login_template():
    return render_template('login.html')# flask nows that this lives in the template folder


@app.route('/register') #www.mysite.com/api/
def register_template():
    return render_template('register.html')

@app.before_first_request
def initialise_database():
    Database.initialise('webdeveloping')

@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']
    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None

    return render_template("profile.html", email=session['email'])

@app.route('/auth/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']
    User.register(email, password)
    return render_template("profile.html", email=session['email'])

@app.route('/blogs/<string:user_id>')
@app.route('/blogs')
def user_blogs(user_id=None):
    if user_id is not None:
        user = User.get_by_id(user_id)
    else:
        user = User.get_by_email(session['email']) #if user is None, you are accesing your own blog

    blogs = user.get_blogs()

    return render_template("user_blogs.html", blogs=blogs, email=user.email)


@app.route('/posts/<string:blog_id>')
def blog_posts(blog_id):
    blog = Blog.from_mongo(blog_id)
    posts = blog.get_posts()

    return render_template("posts.html", posts=posts, blog_title=blog.title)


if __name__ == '__main__':
    app.run(port=4995, debug=True)
