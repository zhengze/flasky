#coding:utf8

from flask import Flask
from config import config

config_name = 'development'
app = Flask(__name__)
#app.config.from_envvar('ZHENMIAO_SETTINGS', silent=True)
app.config.from_object(config[config_name])
