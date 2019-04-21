from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, RadioField, validators
from application.auth.models import User
from flask_login import current_user

class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False

class UserForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2)])
    e_mail = StringField("Sähkoposti", [validators.Length(min=4), validators.Email(message='Virheellinen sähköpostiosoite.')])
    address = StringField("Osoite", [validators.Length(min=5)])
    username = StringField("Käyttäjätunnus", [validators.Length(min=5)])
    password = StringField("Salasana", [validators.Length(min=5)])
    role = RadioField("Rooli", choices=[("CUSTOMER","Asiakas"),("ADMIN","Työntekijä")])

    class Meta:
        csrf = False

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None and current_user.is_authenticated and username.data != User.query.get(current_user.get_id()).username:
            raise validators.ValidationError('Käyttätunnus on jo käytössä.')
        elif user is not None and current_user.is_authenticated is False: 
            raise validators.ValidationError('Käyttätunnus on jo käytössä.')