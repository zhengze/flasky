# -*- coding: utf-8 -*-

from flask import render_template, abort, redirect, url_for, make_response, \
    g, request, session, flash
from contextlib import closing
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from .forms import EntryForm
from . import main
from app import db
from ..models import User, Entry


@main.errorhandler(404)
def page_not_found(error):
    #return render_template('page_not_found.html'), 404
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

@main.route('/', methods=['GET'])
def show_entries():
    entries = Entry.query.all()
    entries_count = Entry.query.count()
    form = EntryForm()
    return render_template('show_entries.html', entries=entries, form=form, entries_count=entries_count)

@main.route('/add', methods=['POST'])
@login_required
def add_entry():
    entryform = EntryForm(request.form)
    entry = Entry(entryform.title.data, entry.text.data)
    db.session.add(entry)
    db.session.commit()
    #flash('New entry was successfully posted')
    return redirect(url_for('main.show_entries'))


