import pyperclip
class Credentials:
    '''
    Class that creates accounts and authenticates the users
    '''
    users_list=[]

    def __init__(self, identify, user_name, password):
        '''
        Initalizing the variables
        '''
        self.identify = identify
        self.user_name = user_name
        self.password = password

    def create_account(self):
        '''
        create and save login credentials for the different users
        '''
        Credentials.users_list.append(self)

    @classmethod
    def authenticate_account(cls, name, key):
        '''
        Method that checks if the username and password are correct
        '''
        for user in cls.users_list:
            if user.user_name == name and user.password == key:
                return user
        return 0