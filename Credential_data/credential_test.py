import unittest
from credential import Credential

class TestCredential(unittest.TestCase):

    def setUp(self):

        self.new_credential = Credential("Name", "password")

    def tearDown(self):

        Credential.credential_list = []

    def test_init(self):

        self.assertEqual(self.new_credential.Name,"Name")
        self.assertEqual(self.new_credential.password,"password")

    def test_save_multiple_credentials(self):

        self.new_credential.save_credential()
        test_credential = Credential("Test","password")
        test_credential.save_credential()

        self.assertEqual(len(Credential.credential_list),2)

    def test_delete_credential(self):

        self.new_credential.save_credential()
        test_credential = Credential("Test","password")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)


if __name__ == '__main__':
    unittest.main() 
