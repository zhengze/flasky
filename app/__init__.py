#coding:utf8

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail
from config import config

db = SQLAlchemy()
moment = Moment()
mail = Mail()
bootstrap = Bootstrap()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    #config[config_name].init_app(app)

    db.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)

    from .api import api as api_blueprint
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint

    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    app.register_blueprint(main_blueprint, url_prefix="/")
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    return app
    
