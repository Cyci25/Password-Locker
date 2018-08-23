import pyperclip
class User:
    """
    Class that generates new instances of users.
    """
    contact_list = [] # Empty contact list

    def __init__(self,first_name,last_name,number,email,account):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
        self.account = account