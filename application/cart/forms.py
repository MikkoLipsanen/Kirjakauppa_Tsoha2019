from flask_wtf import FlaskForm
from wtforms import Form, SelectField, StringField, IntegerField, DecimalField, BooleanField, validators

class CartForm(FlaskForm):
    title = StringField("Nimi", [validators.Length(min=2)])
    author = StringField("Kirjoittaja", [validators.Length(min=2)])
    year = IntegerField("Julkaisuvuosi", [validators.InputRequired()])
    language = StringField("Kieli", [validators.Length(min=3)])
    price = DecimalField("Hinta", [validators.InputRequired()])
    total_price = DecimalField("Hinta", [validators.InputRequired()])

    class Meta:
        csrf = False