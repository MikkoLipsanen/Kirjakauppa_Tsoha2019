from flask import render_template
from application import app
from application.order.models import Order

@app.route("/")
def index():
    return render_template("index.html", recommendations=Order.recommendations())