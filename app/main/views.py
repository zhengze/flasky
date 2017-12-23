# -*- coding: utf-8 -*-

from flask import render_template, abort, redirect, url_for, make_response, \
    g, request, session, flash
from contextlib import closing
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from .forms import EntryForm
from . import main
from ..models import User, Entries


@main.before_request
def before_request():
    g.user = current_user

@main.errorhandler(404)
def page_not_found(error):
    #return render_template('page_not_found.html'), 404
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

@main.route('/')
def show_entries():
    entries = Entries.query.all()
    entries_count = Entries.query.count()
    form = EntryForm()
    return render_template('show_entries.html', entries=entries, form=form, entries_count=entries_count)

@main.route('/add', methods=['POST'])
@login_required
def add_entry():
    #if not g.user.is_authenticated():
    #    abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
            [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


