#coding:utf8

from wtforms import Form, BooleanField, TextField, PasswordField, \
    TextAreaField, validators


class EntryForm(Form):
    title = TextField(u'标题')
    text = TextAreaField(u'正文', [validators.optional(), validators.length(max=200)])
