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
    name = StringField("Nimi", [validators.DataRequired(message='Pakollinen kenttä'), validators.Length(min=2, max=40, message='Hyväksytty pituus 2-40 merkkiä.')])
    e_mail = StringField("Sähkoposti", [validators.DataRequired(message='Pakollinen kenttä'), validators.Length(min=4, max=40, message='Hyväksytty pituus 4-40 merkkiä.'), validators.Email(message='Virheellinen sähköpostiosoite.')])
    address = StringField("Osoite", [validators.DataRequired(message='Pakollinen kenttä'), validators.Length(min=5, max=100, message='Hyväksytty pituus 5-100 merkkiä.')])
    username = StringField("Käyttäjätunnus", [validators.DataRequired(message='Pakollinen kenttä'), validators.Length(min=5, max=50, message='Hyväksytty pituus 5-50 merkkiä.')])
    password = StringField("Salasana", [validators.Length(min=5, max=40, message='Hyväksytty pituus 5-40 merkkiä.')])
    role = RadioField("Rooli", choices=[("CUSTOMER","Asiakas"),("ADMIN","Työntekijä")])

    class Meta:
        csrf = False

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None and current_user.is_authenticated and username.data != User.query.get(current_user.get_id()).username:
            raise validators.ValidationError('Käyttätunnus on jo käytössä.')
        elif user is not None and current_user.is_authenticated is False: 
            raise validators.ValidationError('Käyttätunnus on jo käytössä.')