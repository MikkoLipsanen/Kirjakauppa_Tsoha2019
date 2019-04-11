from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, RadioField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False

class UserForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2)])
    e_mail = StringField("Sähkoposti", [validators.Length(min=4)])
    address = StringField("Osoite", [validators.Length(min=5)])
    username = StringField("Käyttäjätunnus", [validators.Length(min=5)])
    password = StringField("Salasana", [validators.Length(min=5)])
    role = RadioField("Rooli", choices=[("CUSTOMER","Asiakas"),("ADMIN","Työntekijä")])

    class Meta:
        csrf = False