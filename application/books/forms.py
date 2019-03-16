from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, BooleanField, validators

class BookForm(FlaskForm):
    title = StringField("Nimi", [validators.Length(min=2)])
    author = StringField("Kirjoittaja", [validators.Length(min=2)])
    year = IntegerField("Julkaisuvuosi", [validators.InputRequired()])
    language = StringField("Kieli", [validators.Length(min=3)])
    price = DecimalField("Hinta", [validators.InputRequired()])
    available = BooleanField("Varastossa", default="checked")


    class Meta:
        csrf = False