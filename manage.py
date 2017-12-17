from init import *
from views import *
from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand

def make_shell_context():
    return dict(app=app, db=db)

app.debug = True
manager = Manager(app)
manager.add_option('-c', '--config', dest='config', required=False)
manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=make_shell_context))
server = Server(host='0.0.0.0', port=5000)
manager.add_command('runserver', server)

if __name__ == '__main__':
    manager.run()
