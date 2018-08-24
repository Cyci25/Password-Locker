import unittest 
from user import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_user = User("Cynthia","Muriithi","0712873465","c2muriithi@gmail.com","Instagram") # create user object

    def tearDown(self):
        '''
        tearDown method that cleans up after each test case has run       
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Cynthia")
        self.assertEqual(self.new_user.last_name,"Muriithi")
        self.assertEqual(self.new_user.phone_number,"0712873465")
        self.assertEqual(self.new_user.email,"c2muriithi@gmail.com")
        self.assertEqual(self.new_user.account,"Instagram")

    def test_save_multiple_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        
        self.new_user.save_user()
        test_user = User("Test","user","0712873465","test@user.com","account")
        test_user.save_user()

        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):

        '''
        test_delete_user test case to test if the user object can be deleted from the user list
        '''

        self.new_user.save_user()
        test_user = User("Test","user","0712873465","test@user.com","account")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_number(self):

        '''
        test to check if we can find a user by their phone numbers and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","user","0712873465","c2muriithi@gmail.com","account")
        test_user.save_user()

        found_user = User.find_by_number("0712873465")

        self.assertEqual(found_user.email,test_user.email)

    
    def test_user_exists(self):

        '''
        test to check if we can return a Boolean if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Test","user","0712873465","c2muriithi@gmail.com","account")
        test_user.save_user()

        user_exists = User.user_exist("0712873465")

        self.assertTrue(user_exists)

    
    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list) 






if __name__ == '__main__':
    unittest.main()