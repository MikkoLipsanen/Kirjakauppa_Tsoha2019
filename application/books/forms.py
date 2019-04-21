from flask_wtf import FlaskForm
from wtforms import Form, SelectField, StringField, IntegerField, DecimalField, BooleanField, validators

class BookForm(FlaskForm):
    title = StringField("Nimi", [validators.Length(min=2)])
    author = StringField("Kirjoittaja", [validators.Length(min=2)])
    year = IntegerField("Julkaisuvuosi", [validators.InputRequired()])
    language = StringField("Kieli", [validators.Length(min=3)])
    price = DecimalField("Hinta", [validators.InputRequired()])
    amount = IntegerField("Kappalemäärä", [validators.InputRequired()])
    available = BooleanField("Varastossa", default="checked")


    class Meta:
        csrf = False

class BookSearchForm(Form):
    choices = [("Nimi", "Nimi"),
               ("Kirjoittaja", "Kirjoittaja")]
    select = SelectField("Etsi kirjaa:", choices=choices)
    search = StringField('')

