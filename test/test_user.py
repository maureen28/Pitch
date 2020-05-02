import unittest
from app.models import User

class TestUser(unittest.TestCase):
      '''
    Test Class to test the behaviour of the User class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_user = User(password = 'banana')
    
    def test_instance(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password
            
        def test_password_verify(self):
            self.assertTrue(self.new_user.verify_password('banana'))