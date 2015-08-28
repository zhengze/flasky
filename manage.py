from init import *
from views import *
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app.debug = True
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run('0.0.0.0')
