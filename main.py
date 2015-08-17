#coding:utf8

from flask import Flask
from config import config

config_name = 'testing'
app = Flask(__name__)
#app.config.from_envvar('ZHENMIAO_SETTINGS', silent=True)
app.config.from_object(config[config_name])
from views import *

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')
