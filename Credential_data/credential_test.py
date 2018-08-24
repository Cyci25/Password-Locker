import unittest
from credential import Credential

class TestCredential(unittest.TestCase):

    def setUp(self):
        self.new_account = Credential("Name", "password")

    def tearDown(self):
        Credential.credential_list = []

    def test_init(self):
        self.assertEqual(self.new_account.Name,"Name")
        self.assertEqual(self.new_account.password,"password")

if __name__ == '__main__':
    unittest.main() 
