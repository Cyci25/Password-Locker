from credential import Credentials
from user import UsersData
import unittest
import pyperclip

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines the test cases for creating and authenticating credentials
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = Credentials(1,"Cynthia","Muriithi")

    def tearDown(self):
        '''
        TearDown method that does clean up after each test case has run.
        '''
        Credentials.users_list = []

    def test_init(self):
        '''
        Test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.identify,1)
        self.assertEqual(self.new_user.user_name,"Cynthia")
        self.assertEqual(self.new_user.password,"Muriithi")

    def test_create(self):
        '''
        Test_create method that checks if the new credential is saved
        '''
        self.new_user.create_account()
        self.assertEqual(len(Credentials.users_list),1)

    def test_authenticate(self):
        '''
        Test_authenticate method that checks if authentication function signs in a user
        '''
        self.new_user.create_account()
        test_account = Credentials(1,"Test","Password")
        test_account.create_account()

        found_user = Credentials.authenticate_account("Test","Password")
        self.assertEqual(found_user.identify , test_account.identify)

if __name__ == "__main__":
    unittest.main()
