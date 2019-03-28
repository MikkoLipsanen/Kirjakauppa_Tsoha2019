from application import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey
from application.auth.models import User
from application.books.models import Book

from sqlalchemy.sql import text

class Cart(db.Model):
    __tablename__ = 'shopping_cart'
    book_id = db.Column(db.Integer, ForeignKey('book.id'), primary_key=True)
    account_id = db.Column(db.Integer, ForeignKey('account.id'), primary_key=True)

    user = relationship(User, backref=backref("shopping_cart", cascade="all, delete-orphan"))
    book = relationship(Book, backref=backref("shopping_cart", cascade="all, delete-orphan"))

    @staticmethod
    def recommendations():
        stmt = text("SELECT Book.title FROM Book WHERE Book.id IN (SELECT book_id FROM shopping_cart GROUP BY book_id ORDER BY COUNT(book_id) DESC LIMIT 3)")
        res = db.engine.execute(stmt)

        return res