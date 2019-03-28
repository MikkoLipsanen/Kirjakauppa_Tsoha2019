from flask import render_template
from application import app
from application.cart.models import Cart

@app.route("/")
def index():
    return render_template("index.html", recommendations=Cart.recommendations())