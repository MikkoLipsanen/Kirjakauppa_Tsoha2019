from application import db
from sqlalchemy.orm import relationship, backref

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    name = db.Column(db.String(144), nullable=False)
    e_mail = db.Column(db.String(144), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    books = db.relationship("Book", secondary='shopping_cart')
    
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

