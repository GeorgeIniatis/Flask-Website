from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from market import app, db
from market.models import User, Item
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm


@app.route('/')
@app.route('/home')
def home_page():
    return render_template("home.html", head_title="Welcome to Jorge's Market")


@app.route('/market', methods=["GET", "POST"])
@login_required
def market_page():
    purchase_item_form = PurchaseItemForm()
    sell_item_form = SellItemForm()

    if request.method == "POST":
        item_name = request.form.get('purchased_item')
        item = Item.query.filter_by(name=item_name).first()
        if item:
            if current_user.can_purchase(item):
                item.assign_ownership(current_user)
                flash(f"Item Purchased Successfully!", category="success")
            else:
                flash(f"Budget too low!", category="danger")
            return redirect(url_for("market_page"))
        else:
            flash(f"This Item Does Not Exist!", category="danger")
            return redirect(url_for("market_page"))

    elif request.method == "GET":
        items = Item.query.all()
        return render_template("market.html", head_title="Market Page", items=items,
                               purchase_item_form=purchase_item_form,
                               sell_item_form=sell_item_form)


@app.route('/register', methods=["GET", "POST"])
def register_page():
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        user_to_create = User(username=register_form.username.data,
                              email=register_form.email.data,
                              password=register_form.password.data)
        db.session.add(user_to_create)
        db.session.commit()

        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in", category="success")
        return redirect(url_for("market_page"))

    # Check if there are any errors
    if register_form.errors != {}:
        for entry in register_form.errors:
            flash(f"Error with {entry.replace('_', ' ')}: {register_form.errors[entry]}", category="danger")

    return render_template("register.html", head_title="Register Page", register_form=register_form)


@app.route('/login', methods=["GET", "POST"])
def login_page():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        attempted_user = User.query.filter_by(username=login_form.username.data).first()
        if attempted_user and attempted_user.check_password(login_form.password.data):
            login_user(attempted_user)
            flash(f"Login Successful!", category="success")
            return redirect(url_for("market_page"))
        else:
            flash(f"Incorrect Username or Password!", category="danger")

    return render_template("login.html", head_title="Login Page", login_form=login_form)


@app.route('/logout')
@login_required
def logout_page():
    logout_user()
    flash(f"Logout Successful!", category="info")
    return redirect(url_for("home_page"))
