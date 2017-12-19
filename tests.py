import os
import zhenmiao
import unittest
import tempfile

class zhenmiaoTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, zhenmiao.app.config['DATABASE'] = tempfile.mkstemp()
        zhenmiao.app.config['TESTING'] = True
        self.app = zhenmiao.app.test_client()
        zhenmiao.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(zhenmiao.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('admin', '1234')
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login('adminx', '1234')
        assert 'Invalid username' in rv.data
        rv = self.login('admin', 'defaultx')
        assert 'Invalid password' in rv.data

if __name__ == '__main__':
    unittest.main()
