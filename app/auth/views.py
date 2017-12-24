from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user
from . import auth
from app import db
from ..models import User
from .forms import RegistrationForm, LoginForm


@auth.route('/register', methods=['GET', 'POST'])
def register():
    error = None

    if request.method == 'POST':
        form = RegistrationForm(request.form)
        if form.validate():
            user = User(email=form.email.data, username=form.username.data, role_id=1)
            user.password = form.password.data
            db.session.add(user)
            db.session.commit()
            
            if user is not None and user.verify_password(form.password.data):
                return redirect(url_for('auth.login'))
            flash('You were logged in')
    else:
        form = RegistrationForm()
        
    return render_template('register.html', error=error, form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('main.show_entries'))

    

@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate():
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None and user.verify_password(form.password.data):
                login_user(user)
                return redirect(url_for('main.show_entries'))
            flash('You were logged in')
    else:
        form = LoginForm()
        
    return render_template('login.html', error=error, form=form)


@auth.route('/logout')
def log_out():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('main.show_entries'))

