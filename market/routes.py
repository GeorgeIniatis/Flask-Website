from flask import render_template
from market import app
from market.models import *


@app.route('/')
@app.route('/home')
def home_page():
    return render_template("home.html", head_title="Home Page", body_title="Home Page")


@app.route('/market')
def market_page():
    items = ItemModel.query.all()
    return render_template("market.html", head_title="Market Page", body_title="Market Page", items=items)
