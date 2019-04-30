from flask import Flask

from src.common.database import Database

__author__ = "janao"

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = '123'  #this is the key to secure the cookie


@app.before_first_request
def init_db():
    Database.initialize()



from src.models.users.views import user_blueprint
app.register_blueprint(user_blueprint, url_prefix="/users")



