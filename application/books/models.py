from application import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(150), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    available = db.Column(db.Boolean, nullable=False)

    def __init__(self, title, author, year, language, price, available):
        self.title = title
        self.author = author
        self.year = year
        self.language = language
        self.price = price
        self.available = True