from flask import Flask, render_template
from src.common.database import Database

__author__ = "janao"

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = '123'  #this is the key to secure the cookie


@app.before_first_request
def init_db():
    Database.initialize()

@app.route('/')
def home():
    return render_template('home.html')



from src.models.users.views import user_blueprint
from src.models.stores.views import store_blueprint
from src.models.alerts.views import alert_bleuprint

app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(store_blueprint, url_prefix="/stores")
app.register_blueprint(alert_bleuprint, url_prefix="/alerts")



