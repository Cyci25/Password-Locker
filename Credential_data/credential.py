class Credential:

    def __init__(self,Name,password):
        self.Name = Name
        self.password = password

    credential_list = []

    def save_credential(self):
        Credential.credential_list.append(self)
    
    # def delete_new_credential(self):
    #     Credential.credential_list.remove(self)