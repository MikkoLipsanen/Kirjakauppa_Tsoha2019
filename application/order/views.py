from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user

from application import app, db, login_required
from application.books.models import Book
from application.auth.models import User
from application.order.models import Order
from application.order.forms import OrderForm, OrdersForm

@app.route("/order", methods=['GET', 'POST'])
@login_required(role="CUSTOMER")
def order_create():
    user = User.query.get(current_user.get_id())
    form = OrderForm(obj=user)
    books = user.books
    totalPrice = sum(Book.price for Book in books)
    if request.method == 'POST' and form.validate():
        form = OrderForm(request.form)
        o = Order(form.name.data, form.e_mail.data, form.address.data, totalPrice)
        print(o.name)
        o.user_id = current_user.id
        for book in books:
            o.books.append(book)
        db.session().add(o)
        db.session().commit()
        user.books.clear()
        db.session().add(user)
        db.session().commit()
        return redirect(url_for("books_index"))
    else:
        return render_template("order/order.html", books=books, price=totalPrice, form=form)

@app.route("/orders", methods=['GET'])
@login_required(role="CUSTOMER")
def order_index():
    user = User.query.get(current_user.get_id())
    form = OrdersForm(request.form)
    orders = user.orders
    size = len(orders)
    price = sum(Order.price for Order in orders)
    return render_template("order/list.html", orders=orders, form=form, size=size, sum=price)