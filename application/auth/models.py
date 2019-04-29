from application import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey, Table, Column, Integer

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    name = db.Column(db.String(144), nullable=False)
    e_mail = db.Column(db.String(144), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144), nullable=False)

    books = db.relationship("Book", secondary='shopping_cart')
    roles = db.relationship("Role", secondary='user_role')
    orders = db.relationship("Order", backref='account', lazy=True)

    def __init__(self, name, e_mail, address, username, password):
        self.name = name
        self.e_mail = e_mail
        self.address = address
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
    def has_role(self, role):
        return any(user_role.name == role for user_role in self.roles)


user_role = db.Table('user_role',
    db.Column('account_id', db.Integer, db.ForeignKey('account.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True)
)

class Role(db.Model):
    
    __tablename__ = "role"
  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


    def __init__(self, name):
        self.name = name