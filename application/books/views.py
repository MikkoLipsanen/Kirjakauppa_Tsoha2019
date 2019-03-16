from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.books.models import Book
from application.books.forms import BookForm

@app.route("/books", methods=["GET"])
def books_index():
    return render_template("books/list.html", books = Book.query.all())

@app.route("/books/new/")
@login_required
def books_form():
    return render_template("books/new.html", form = BookForm())

@app.route("/books/<book_id>/", methods=["POST"])
@login_required
def books_set_unavailable(book_id):

    b = Book.query.get(book_id)

    if b.available == False:
        b.available = True
    elif b.available == True:
        b.available = False

    db.session().commit()
  
    return redirect(url_for("books_index"))

@app.route("/books/", methods=["POST"])
@login_required
def books_create():
    form = BookForm(request.form)

    if not form.validate():
        return render_template("books/new.html", form = form)
        
    b = Book(form.title.data, form.author.data, form.year.data, form.language.data, form.price.data,
    form.available.data)

    db.session().add(b)
    db.session().commit()
  
    return redirect(url_for("books_index"))