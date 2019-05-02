from flask_wtf import FlaskForm
from wtforms import SelectField, StringField,  DecimalField, IntegerField, DateTimeField, validators

class OrderForm(FlaskForm):
    name = StringField("Nimi", [validators.DataRequired(message='Pakollinen kenttä'), validators.Length(min=2, max=40, message='Hyväksytty pituus 2-40 merkkiä.')])
    e_mail = StringField("Sähkoposti", [validators.DataRequired(message='Pakollinen kenttä'), validators.Length(min=4, max=40, message='Hyväksytty pituus 4-40 merkkiä.'), validators.Email(message='Virheellinen sähköpostiosoite.')])
    address = StringField("Osoite", [validators.DataRequired(message='Pakollinen kenttä'), validators.Length(min=5, max=100, message='Hyväksytty pituus 5-100 merkkiä.')])

    class Meta:
        csrf = False

class OrdersForm(FlaskForm):
    id = IntegerField("Tunnus", [validators.DataRequired(message='Pakollinen kenttä')])
    name = StringField("Nimi", [validators.DataRequired(message='Pakollinen kenttä')])
    date = DateTimeField("Tilattu", [validators.DataRequired(message='Pakollinen kenttä')])
    price = DecimalField("Hinta", [validators.DataRequired(message='Pakollinen kenttä')])

    class Meta:
        csrf = False