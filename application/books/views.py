from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required

from application import app, db
from application.books.models import Book
from application.books.forms import BookForm, BookSearchForm

@app.route("/books", methods=['GET', 'POST'])
def books_index():
    search = BookSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template("books/list.html", books = Book.query.all(), form=search)

@app.route("/books/results")
def search_results(search):
    results = []
    search_string = search.data['search']

    if search_string:
        if search.data['select'] == 'Nimi':
            qry = db.session().query(Book).filter(Book.title.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Kirjoittaja':
            qry = db.session().query(Book).filter(Book.author.contains(search_string))
            results = qry.all()
    if not results:
        flash('Ei osumia')
        return redirect(url_for("books_index"))
    else:
        return render_template("books/list.html", books = results, form=search)

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

@app.route("/book/", methods=["GET"])
def book_view():
    book_id = request.args.get("book_id")
    return render_template('books/book.html', book = Book.query.get(book_id), form=BookForm())

@app.route("/books/delete/<book_id>/", methods=["POST"])
@login_required
def books_delete(book_id):
    b = Book.query.get(book_id)
    db.session().delete(b)

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

@app.route("/books/edit/", methods=["GET", "POST"])
def books_edit():
    id = request.args.get("book_id")
    book = Book.query.get(id)
    form = BookForm(obj=book)
    if request.method == 'POST' and form.validate():
        form.populate_obj(book)
        db.session().commit()
        flash('Kirjan tiedot paivitetty!')
        return redirect(url_for("books_index"))
    return render_template('books/edit.html', form=form)
