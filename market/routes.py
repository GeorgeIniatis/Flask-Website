from flask import render_template, redirect, url_for
from market import app, db
from market.models import *
from market.forms import *


@app.route('/')
@app.route('/home')
def home_page():
    return render_template("home.html", head_title="Home Page")


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template("market.html", head_title="Market Page", items=items)


@app.route('/register', methods=["GET", "POST"])
def register_page():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        user_to_create = User(username=register_form.username.data,
                              email=register_form.email.data,
                              password_hash=register_form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for("market_page"))

    if register_form.errors != {}:  # If there are errors from the validations
        for error_message in register_form.errors.values():
            print(f"Error in register page: {error_message}")

    return render_template("register.html", head_title="Register Pge", register_form=register_form)
