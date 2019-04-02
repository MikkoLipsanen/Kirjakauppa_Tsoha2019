from flask_wtf import FlaskForm
from wtforms import SelectField, StringField,  DecimalField, IntegerField, DateTimeField, validators

class OrderForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2)])
    e_mail = StringField("Sahkoposti", [validators.Length(min=4)])
    address = StringField("Osoite", [validators.Length(min=5)])
    #total_price = DecimalField("Hinta", [validators.InputRequired()])

    class Meta:
        csrf = False

class OrdersForm(FlaskForm):
    id = IntegerField("Tunnus", [validators.InputRequired()])
    date = DateTimeField("Tilattu", [validators.InputRequired()])
    price = DecimalField("Hinta", [validators.InputRequired()])

    class Meta:
        csrf = False