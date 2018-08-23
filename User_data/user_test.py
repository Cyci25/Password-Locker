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


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Cynthia")
        self.assertEqual(self.new_user.last_name,"Muriithi")
        self.assertEqual(self.new_user.phone_number,"0712873465")
        self.assertEqual(self.new_user.email,"c2muriithi@gmail.com")
        self.assertEqual(self.new_user.account,"Instagram")

if __name__ == '__main__':
    unittest.main()