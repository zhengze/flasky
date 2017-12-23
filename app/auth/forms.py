from flask_wtf import Form
from wtforms import StringField, BooleanField, TextField, PasswordField, SubmitField, validators
from wtforms.validators import Required, Length, Email


class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
            validators.Required(),
            validators.EqualTo('confirm', message='Passwords must match')
            ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField(u'Password', validators=[Required()])
    remember_me = BooleanField(u'Keep me logged in')
    submit = SubmitField('Log In')
