from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user
from sqlalchemy.sql import func

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
            item = Book.query.get(book.id)
            item.amount -= 1 
        db.session().add(o)
        db.session().commit()
        user.books.clear()
        db.session().add(user)
        db.session().commit()
        return redirect(url_for("books_index"))
    else:
        return render_template("order/order.html", books=books, price=format(totalPrice, '.2f'), form=form)

@app.route("/orders", methods=['GET'])
@login_required(role="CUSTOMER")
def order_index():
    user = User.query.get(current_user.get_id())
    form = OrdersForm(request.form)
    orders = user.orders
    size = len(orders)
    price = sum(Order.price for Order in orders)
    return render_template("order/list.html", orders=orders, form=form, size=size, sum=format(price, '.2f'))

@app.route("/orders/list", methods=['GET'])
@login_required(role="ADMIN")
def order_list():
    form = OrdersForm(request.form)
    orders = Order.query.all()
    price = sum(Order.price for Order in orders)
    if len(orders) > 0:
        average = price / len(orders)
    else:
        average = 0
    return render_template("order/total.html", orders=orders, form=form, sum=format(price, '.2f'), avg=format(average, '.2f'))

@app.route("/orders/delete/<order_id>/", methods=["POST"])
@login_required(role="ADMIN")
def order_delete(order_id):
    order = Order.query.get(order_id)
    db.session().delete(order)

    db.session().commit()

    return redirect(url_for("order_list"))