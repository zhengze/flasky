#coding:utf8

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import g
from init import config_name, app
from config import config
import sqlite3

DB_CONNECT_STRING = config[config_name].SQLALCHEMY_DATABAASE_URI
engine = create_engine(DB_CONNECT_STRING, convert_unicode=True, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                      bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # 在这里导入定义模型所需要的所有模块，这样它们就会正确的注册在
    # 元数据上。否则你就必须在调用 init_db() 之前导入它们。
    import models
    Base.metadata.create_all(bind=engine)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.before_request
def before_request():
    if config_name == 'testing':
        g.db = connect_db()
    else:
        g.db = db_session

