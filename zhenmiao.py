# -*- coding: utf-8 -*-

import sqlite3
from flask import Flask, render_template, abort, redirect, url_for, make_response, \
    g, request, session, flash
from contextlib import closing

# configuration
DATABASE = '/tmp/zhenmiao.db'
DEBUG = True
SECRET_KEY = '78b32ed2bbb83f84d3d067ce3463d2aa943c7609'
USERNAME = 'admin'
PASSWORD = '1234'

app = Flask(__name__)
#app.config.from_envvar('ZHENMIAO_SETTINGS', silent=True)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()

@app.errorhandler(404)
def page_not_found(error):
    #return render_template('page_not_found.html'), 404
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

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
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')
