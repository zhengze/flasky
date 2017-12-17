from init import *
from views import *
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand

app.debug = True
manager = Manager(app)
manager.add_command('db', MigrateCommand)
server = Server(host='0.0.0.0', port=5000)
manager.add_command('runserver', server)

if __name__ == '__main__':
    manager.run()
