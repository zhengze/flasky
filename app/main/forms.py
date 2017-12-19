#coding:utf8

from wtforms import Form, BooleanField, TextField, PasswordField, \
    TextAreaField, validators

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
    username = TextField(u'用户名', [validators.Length(min=4, max=25)])
    password = PasswordField(u'密码')

class EntryForm(Form):
    title = TextField(u'标题')
    text = TextAreaField(u'正文', [validators.optional(), validators.length(max=200)])
