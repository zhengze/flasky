# -*- coding: utf-8 -*-

import sqlite3
from flask import render_template, abort, redirect, url_for, make_response, \
    g, request, session, flash
from contextlib import closing
from flask.ext.login import LoginManager, login_user, logout_user, current_user
from forms import LoginForm, EntryForm
from main import app
from database import db_session
from models import User, Entries

#def init_db():
#    with closing(connect_db()) as db:
#        with app.open_resource('schema.sql', mode='r') as f:
#            db.cursor().executescript(f.read())
#        db.commit()

@app.before_request
def before_request():
    g.user = current_user

@app.errorhandler(404)
def page_not_found(error):
    #return render_template('page_not_found.html'), 404
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

@app.route('/')
def show_entries():
    #cur = g.db.execute('select title, text from entries order by id desc')
    #entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    entries = Entries.query.all()
    form = EntryForm()
    return render_template('show_entries.html', entries=entries, form=form)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            #session['logged_in'] = True
            g.user = current_user
            user = User.query.filter_by(username=username).first()
            login_user(user)
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    else:
        form = LoginForm()
        
    return render_template('login.html', error=error, form=form)


@app.route('/logout')
def logout():
    #session.pop('logged_in', None)
    logout_user()
    flash('You were logged out')
    return redirect(url_for('show_entries'))

