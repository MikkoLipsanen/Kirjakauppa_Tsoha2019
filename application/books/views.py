from application import app, db
from flask import redirect, render_template, request, url_for
from application.books.models import Book

@app.route("/books", methods=["GET"])
def books_index():
    return render_template("books/list.html", books = Book.query.all())

@app.route("/books/new/")
def books_form():
    return render_template("books/new.html")

@app.route("/books/<book_id>/", methods=["POST"])
def books_set_unavailable(book_id):

    b = Book.query.get(book_id)

    if b.available == False:
        b.available = True
    elif b.available == True:
        b.available = False

    db.session().commit()
  
    return redirect(url_for("books_index"))

@app.route("/books/", methods=["POST"])
def books_create():

    print("REQUEST: ", request.form)
    b = Book(request.form.get('title'), request.form.get("author"), 
    request.form.get("year"), request.form.get("language"), request.form.get("price"),
    request.form.get("available"))

    db.session().add(b)
    db.session().commit()
  
    return redirect(url_for("books_index"))