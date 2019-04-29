from flask_wtf import FlaskForm
from wtforms import Form, SelectField, StringField, IntegerField, DecimalField, BooleanField, validators

class BookForm(FlaskForm):
    title = StringField("Nimi", [validators.Length(min=2, max=50, message='Hyväksytty pituus 2-50 merkkiä.')])
    author = StringField("Kirjoittaja", [validators.Length(min=2, max=50, message='Hyväksytty pituus 2-50 merkkiä.')])
    year = IntegerField("Julkaisuvuosi", [validators.DataRequired(message='Pakollinen kenttä'), validators.NumberRange(min=0, max=2019, message='Vuoden oltava välillä 0-2019.')])
    language = StringField("Kieli", [validators.Length(min=3, max=30, message='Hyväksytty pituus 2-30 merkkiä.')])
    price = DecimalField("Hinta", [validators.DataRequired(message='Pakollinen kenttä'), validators.NumberRange(min=0, max=10000, message='Hinnan oltava välillä 0-10000 euroa.')])
    amount = IntegerField("Kappalemäärä", [validators.DataRequired(message='Pakollinen kenttä'), validators.NumberRange(min=0, max=10000, message='Määrän oltava välillä 0-10000 kappaletta.')])
    available = BooleanField("Varastossa", default="checked")


    class Meta:
        csrf = False

class BookSearchForm(Form):
    choices = [("Nimi", "Nimi"),
               ("Kirjoittaja", "Kirjoittaja")]
    select = SelectField("Etsi kirjaa:", choices=choices)
    search = StringField('', [validators.Length(max=60, message='Hakusanan maksimipituus 60 merkkiä')])

