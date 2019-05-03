from application import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey, Table, Column, Integer
from sqlalchemy.sql import func, text
from datetime import date

class Order(db.Model):

    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, server_default=func.now())
    name = db.Column(db.String(144), nullable=False)
    e_mail = db.Column(db.String(144), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    books = db.relationship("Book", secondary='order_item')

    def __init__(self, name, e_mail, address, price):
        self.name = name
        self.e_mail = e_mail
        self.address = address
        self.price = price

    class Meta:
        ordering = ('-date_created', )

    @staticmethod
    def recommendations():
        stmt = text("SELECT Book.title, Book.id FROM Book WHERE Book.id IN (SELECT book_id FROM order_item GROUP BY book_id ORDER BY COUNT(book_id) DESC LIMIT 3)")
        res = db.engine.execute(stmt)

        return res
    
    @staticmethod
    def registrations_per_day():
        stmt = text("SELECT COUNT(date_created) AS registrations, date_created AS datetime FROM account GROUP BY DATE(date_created)")
        res = db.engine.execute(stmt)

        return res
     
class OrderItem(db.Model):

    __tablename__ = 'order_item'

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)

    book = db.relationship("Book", backref=backref('order_item', cascade="all, delete-orphan"))
    order = db.relationship("Order", backref=backref('order_item', cascade="all, delete-orphan"))