from flask import Flask
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"    
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# sovelluksen toiminnallisuudet
from application import views

from application.books import models
from application.books import views

from application.auth import models 
from application.auth import views

from application.cart import models 
from application.cart import views

from application.order import models 
from application.order import views

# kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Toiminto vaatii kirjautumisen."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try: 
    db.create_all()
except:
    pass