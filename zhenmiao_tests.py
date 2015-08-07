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

if __name__ == '__main__':
    unittest.main()
