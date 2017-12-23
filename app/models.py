from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager, db


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.String(50), unique=True, nullable=False)
    users = db.relationship('User', backref=db.backref('role', lazy='dynamic'))

    def __repr__(self):
        return '<Role %r>' % (self.rolename)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.Integer, db.ForeignKey('role.id'))

    #def __init__(self, username=None, password=None, email=None):
    #    self.username = username
    #    self.password = password
    #    self.email = email
    
    @property
    def password(self):
        raise AttributeError('password is not a readable property')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % (self.username)

class Entries(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50)) 
    text = db.Column(db.Text)
    
    def __repr__(self):
        return '<Entry %r>' %(self.title)


    
