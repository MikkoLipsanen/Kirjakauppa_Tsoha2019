from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user

from application import app, db, login_required
from application.books.models import Book
from application.auth.models import User
from application.cart.forms import CartForm

@app.route("/cart", methods=['GET'])
@login_required(role="CUSTOMER")
def cart_index():
    user = User.query.get(current_user.get_id())
    form = CartForm(request.form)
    books = user.books
    totalPrice = sum(Book.price for Book in books)
    return render_template("cart/cart.html", books=books, sum=format(totalPrice, '.2f'), form=form)

@app.route("/cart/add/")
@login_required(role="CUSTOMER")
def cart_add():
    id = request.args.get("book_id")
    book = Book.query.get(id)
    user = User.query.get(current_user.get_id())
    user.books.append(book)

    db.session.add(user)
    db.session.commit()

    return redirect(url_for("books_index"))

@app.route("/cart/delete/<book_id>/", methods=["POST"])
@login_required(role="CUSTOMER")
def cart_delete(book_id):
    book = Book.query.get(book_id)
    user = User.query.get(current_user.get_id())
    user.books.remove(book)

    db.session.add(user)
    db.session.commit()
    flash('{} poistettu ostoskorista'.format(book.title))

    return redirect(url_for("cart_index"))

