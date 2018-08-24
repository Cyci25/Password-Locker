class User:
    """
    Class that generates new instances of users.
    """

    def __init__(self,first_name,last_name,number,email,account):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
        self.account = account

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