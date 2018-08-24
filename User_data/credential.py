class Credential:

    credential_list = []
    
    def __init__(self,Name,password):
        self.Name = Name
        self.password = password

    def save_credential(self):
        Credential.credential_list.append(self)
    
    def delete_credential(self):
        Credential.credential_list.remove(self)