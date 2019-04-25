from flask_wtf import FlaskForm
from wtforms import Form, SelectField, StringField, IntegerField, DecimalField, BooleanField, validators

class CartForm(FlaskForm):
    title = StringField("Nimi", [validators.Length(min=2, max=50, message='Hyväksytty pituus 2-50 merkkiä.')])
    author = StringField("Kirjoittaja", [validators.Length(min=2, max=50, message='Hyväksytty pituus 2-50 merkkiä.')])
    year = IntegerField("Julkaisuvuosi", [validators.InputRequired(), validators.NumberRange(min=0, max=2019, message='Vuoden oltava välillä 0-2019.')])
    language = StringField("Kieli", [validators.Length(min=3, max=30, message='Hyväksytty pituus 2-30 merkkiä.')])
    price = DecimalField("Hinta", [validators.InputRequired(), validators.NumberRange(min=0, max=10000, message='Hinnan oltava välillä 0-10000 euroa.')])
  
    class Meta:
        csrf = False