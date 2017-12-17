from sqlalchemy import Table, Column, Integer, String, Text, Unicode, SmallInteger
from sqlalchemy.orm import mapper
from database import db_session, Base
from flask_login import LoginManager, UserMixin
from init import app

ROLE_USER = 0
ROLE_ADMIN = 1

login_manager = LoginManager()
login_manager.setup_app(app)

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)


class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(Unicode(40), nullable=False)
    email = Column(String(120), unique=True)
    role = Column(SmallInteger, default=ROLE_USER)

    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.username)

class Entries(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(String(50)) 
    text = Column(Text)
    
    def __repr__(self):
        return '<Entry %r>' %(self.title)


    
