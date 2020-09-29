from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
db = SQLAlchemy(app)
# db = create_engine("mysql://rohanban_rohan:s1lma549x@nahor.cf:3306/rohanban_nahorcf")

# app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

from .models import Shortify

from .routes import routes as route_blueprint

app.register_blueprint(route_blueprint)