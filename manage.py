#!/usr/bin/env python
#coding: utf-8


import os
from app import create_app, db
from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand

config_name = os.getenv("FLASK_CONFIG") or "default"
app = create_app(config_name)
app.app_context().push()

migrate = Migrate(app, db)
manager = Manager(app)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittests.TextTestRunner(verbosity=2).run(tests)


manager.add_option('-c', '--config', dest='config', required=False)
manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=make_shell_context))
server = Server(host='0.0.0.0', port=5000)
manager.add_command('runserver', server)

if __name__ == '__main__':
    manager.run()
