import unittest
from app.models import Author

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user=Author(password='cows')

    def test_password_setter(self):
        self.assertTrue(self.new_author.author_pass is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_author.password

    def test_password_verification(self):
        self.assertTrue(self.new_author.verify_password('cows'))