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
    DATABASE = '/tmp/zhenmiao.db'
    SQLALCHEMY_DATABAASE_URI = 'sqlite:///' + DATABASE
    USERNAME = 'admin'
    PASSWORD = '1234'

class ProductConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABAASE_URI = 'mysql+pymysql://root:1234@localhost:3306/zhenmiao?charset=utf8'
    

config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductConfig,
}
