from sqlalchemy import Table, Column, Integer, String, Text
from sqlalchemy.orm import mapper
from database import db_session, Base

#class User(Base):
#    __tablename__ = 'users'
#    id = Column(Integer, primary_key=True)
#    name = Column(String(50), unique=True)
#    email = Column(String(120), unique=True)
#
#    def __init__(self, name=None, email=None):
#        self.name = name
#        self.email = email
#
#    def __repr__(self):
#        return '<User %r>' % (self.name)

class Entries(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(String(50)) 
    text = Column(Text)
    
    def __repr__(self):
        return '<Entry %r>' %(self.title)


    
