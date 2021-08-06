from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template("home.html", head_title="Home Page", body_title="Home Page")


@app.route('/market')
def market_page():
    items = [
        {"id": 1, "name": "Phone", "barcode": "951475621452", "price": 450},
        {"id": 2, "name": "Laptop", "barcode": "914756248597", "price": 1200},
        {"id": 3, "name": "Headset", "barcode": "475614785234", "price": 300},
    ]
    return render_template("market.html", head_title="Market Page", body_title="Market Page", items=items)


if __name__ == "__main__":
    app.run(debug=True)
