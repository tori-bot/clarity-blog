import unittest
from app.models import Quotes

class UserModelTest(unittest.TestCase):
    
    def setUp(self):
        self.new_quote=Quotes(quote=2)

    def tearDown(self):
        print('teardown')

    def test_init(self):
        self.assertEqual(self.new_quote.quote,2)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quotes))