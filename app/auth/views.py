from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user
from . import auth
from ..models import User
from .forms import LoginForm


#@auth.before_request
#def before_request():
#    g.user = current_user


@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate():
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None or user.verify_password(form.password.data):
                login_user(user)
                return redirect(url_for('main.show_entries'))
            flash('You were logged in')
    else:
        form = LoginForm()
        
    return render_template('login.html', error=error, form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('main.show_entries'))

