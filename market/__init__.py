from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///market.db'  # Specify position of db and its name
app.config["SECRET_KEY"] = "cdbde4cf31e8c9ec22179fe6"  # os.urandom(12).hex()
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Needs to be after
from market import routes
