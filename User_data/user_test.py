from credential import Credentials
from user import UsersData
import unittest
import pyperclip

class TestUserData(unittest.TestCase):
    '''
    Test class that defines the test cases for creating accounts login credentials
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_data = UsersData(1,1,"Insta","account")

    def tearDown(self):
        '''
        TearDown method that does clean up after each test case has run.
        '''
        UsersData.data_list = []

    def test_init(self):
        '''
        Test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_data.identify,1)
        self.assertEqual(self.new_data.data_id,1)
        self.assertEqual(self.new_data.account,"Insta")
        self.assertEqual(self.new_data.acc_key,"account")

    def test_add_password(self):
        '''
        test_add_password method checks if the account and password can be saved
        '''
        self.new_data.add_password()
        self.assertEqual(len(UsersData.data_list),1)

    def test_display_data(self):
        '''
        Test_display_data mehtod checks if the data saved can be displayed.
        '''
        self.new_data.add_password()
        test_data = UsersData(1,1,"Insta","account")
        test_data.add_password()

        data_found = UsersData.display_data(1,1)
        self.assertEqual(data_found.account,test_data.account)

    def test_data_exists(self):
        '''
        Test_data_exists method checks if the function for checking data saved works
        '''
        self.new_data.add_password()
        test_data = UsersData(1,1,"Insta","account")
        test_data.add_password()

        data_exists = UsersData.existing_data(1)
        self.assertTrue(data_exists)

    def test_copy_password(self):
        '''
        Test_copy_password method checks if the copy password function works
        '''
        self.new_data.add_password()
        UsersData.copy_password(1,1)

        self.assertEqual(self.new_data.acc_key,pyperclip.paste())


if __name__ == "__main__":
    unittest.main()