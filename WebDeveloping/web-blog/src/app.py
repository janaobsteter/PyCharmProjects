<<<<<<< HEAD
from flask import Flask, render_template, request, session, make_response, Blueprint
=======
from flask import Flask, render_template, request, session
>>>>>>> a960e91a7e7f979d8e86921c1c861db15f8a5d79

#use Flask to define app
#creating Flask application
from src.common.database import Database
<<<<<<< HEAD
from src.modules.blog import Blog
from src.modules.post import Post
from src.modules.user import User


app = Flask(__name__) # '__main__'
app.secret_key = "janao"

#create API endpoints
@app.route('/') #www.mysite.com/api/
def home_template():
    return render_template('home.html')# flask nows that this lives in the template folder
=======
from src.modules.user import User

app = Flask(__name__) # '__main__'
#we have to add the secret key - to make sure that the cookie we are sending is secure
app.secret_key = "janao"


#create API endpoints
@app.route('/')
def home_template():
    return render_template('home.html')
>>>>>>> a960e91a7e7f979d8e86921c1c861db15f8a5d79

@app.route('/login') #www.mysite.com/api/
def login_template():
    return render_template('login.html')# flask nows that this lives in the template folder

<<<<<<< HEAD

@app.route('/register') #www.mysite.com/api/
def register_template():
    return render_template('register.html')

@app.before_first_request
def initialise_database():
    Database.initialise('webdeveloping')

@app.route('/auth/login', methods=['POST'])
=======
@app.route('/register') #www.mysite.com/api/
def register_template():
    return render_template('register.html')# flask nows that this lives in the template folder

@app.before_first_request #IT will run the method before the first request
def initialise_database():
    Database.initialise("webdeveloping")


@app.route('/auth/login', methods = ['POST']) #we are accepting only post requests
>>>>>>> a960e91a7e7f979d8e86921c1c861db15f8a5d79
def login_user():
    email = request.form['email']
    password = request.form['password']
    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None
<<<<<<< HEAD

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

    return render_template("posts.html", posts=posts, blog_title=blog.title, blog_id=blog._id)

@app.route('/blogs/new', methods=['POST', 'GET']) #if the method is get, the user just arrived at the end point; is POST, the user clicked submit
def create_new_blog():
    if request.method == 'GET':
        return render_template('new_blog.html')
    else:
        #accept the data
        title = request.form['title']
        description = request.form['description']
        user = User.get_by_email(session['email'])

        new_blog = Blog(user.email, user._id, title, description)
        new_blog.save_to_mongo()

        return make_response(user_blogs(user._id))\

@app.route('/posts/new/<string:blog_id>', methods=['POST', 'GET']) #if the method is get, the user just arrived at the end point; is POST, the user clicked submit
def create_new_post(blog_id):
    if request.method == 'GET':
        return render_template('new_post.html', blog_id=blog_id)
    else:
        #accept the data
        title = request.form['title']
        content = request.form['content']
        user = User.get_by_email(session['email'])

        new_post = Post(blog_id, title, content, user.email)
        new_post.save_to_mongo()

        return make_response(blog_posts(blog_id))



if __name__ == '__main__':
    app.run(port=4995, debug=True)
=======
    return render_template("profile.html", email = session['email'])


@app.route('/auth/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']
    User.register(email, password)
    return render_template("profile.html", email = session['email'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)
>>>>>>> a960e91a7e7f979d8e86921c1c861db15f8a5d79
