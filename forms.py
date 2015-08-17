#coding:utf8

from wtforms import Form, BooleanField, TextField, PasswordField, validators

class LoginForm(Form):
    username = TextField('用户名', [validators.Length(min=4, max=25)])
    password = PasswordField('密码')
