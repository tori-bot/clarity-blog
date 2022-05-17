import unittest
from app.models import Blog

class UserModelTest(unittest.TestCase):
    
    def setUp(self):
        self.new_blog=Blog(title='girls')

    def tearDown(self):
        print('teardown')

    def test_init(self):
        self.assertEqual(self.new_blog.title,'girls')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))