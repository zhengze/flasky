# configuration

class TestingConfig(object):
    DATABASE = '/tmp/zhenmiao.db'
    DEBUG = True
    SECRET_KEY = '78b32ed2bbb83f84d3d067ce3463d2aa943c7609'
    USERNAME = 'admin'
    PASSWORD = '1234'
    CSRF_ENABLED = True

config = {
    'testing': TestingConfig
}
