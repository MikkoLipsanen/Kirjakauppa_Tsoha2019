from application import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey
from application.auth.models import User
from application.books.models import Book

class Cart(db.Model):
    __tablename__ = 'shopping_cart'
    book_id = db.Column(db.Integer, ForeignKey('book.id'), primary_key=True)
    account_id = db.Column(db.Integer, ForeignKey('account.id'), primary_key=True)

    user = relationship(User, backref=backref("shopping_cart", cascade="all, delete-orphan"))
    book = relationship(Book, backref=backref("shopping_cart", cascade="all, delete-orphan"))

