from flask_login import UserMixin
from app import login_manager, db

ROLE_USER = 0
ROLE_ADMIN = 1


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.Unicode(40), nullable=False)
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)

    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.username)

class Entries(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50)) 
    text = db.Column(db.Text)
    
    def __repr__(self):
        return '<Entry %r>' %(self.title)


    
