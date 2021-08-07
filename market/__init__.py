from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///market.db'  # Specify position of db and its name
db = SQLAlchemy(app)

from market import routes
