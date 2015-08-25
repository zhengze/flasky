# configuration

class Config(object):
    DEBUG = False
    SECRET_KEY = '78b32ed2bbb83f84d3d067ce3463d2aa943c7609'
    CSRF_ENABLED = True
    
class TestingConfig(Config):
    DATABASE = '/tmp/zhenmiao.db'
    SQLALCHEMY_DATABAASE_URI = 'sqlite:///' + DATABASE
    USERNAME = 'admin'
    PASSWORD = '1234'

class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
}
