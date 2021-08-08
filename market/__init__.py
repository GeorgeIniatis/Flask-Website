from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///market.db'  # Specify position of db and its name
app.config["SECRET_KEY"] = "cdbde4cf31e8c9ec22179fe6" # os.urandom(12).hex()
db = SQLAlchemy(app)

from market import routes
