class User:
    """
    Class that generates new instances of users.
    """

    def __init__(self,first_name,last_name,number,email,account,Password,user_name):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
        self.account = account
        self.Password = Password
        self.user_name = user_name

    user_list = [] # Empty user list

    def save_user(self):
        '''
        save_user method saves user object into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes user object into user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        '''
            Method that takes in a number and returns the user that matches that number.

            Args:
                number: Phone number to search for
            Returns :
                Details of person that matches the number.
        '''    
        for user in cls.user_list:
            if user.phone_number == number:
                return user

    @classmethod
    def user_exist(cls,number):
        '''
        Method that checks if a user exists from the user list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.phone_number == number:
                    return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list   
