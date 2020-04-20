import unittest
from user_credentials import Credentials

class TestCredentials(unittest.TestCase):

  def setUp(self):
    self.new_credential = Credentials("Bree95", "Facebook", "password1")

  def tearDown(self):
    Credentials.credentials_list = []

  def test_init(self):
    self.assertEqual(self.new_credential.user_name, "Bree95")
    self.assertEqual(self.new_credential.account_name, "Facebook")
    self.assertEqual(self.new_credential.password, "password1")

  def test_save_credentials(self):
    self.new_credential.save_credentials()
    self.assertEqual(len(Credentials.credentials_list), 1)

  def test_delete_credentials(self):
    self.new_credential.save_credentials()
    test_credential = Credentials("Brenda", "gmail", "4676jl")
    test_credential.save_credentials()
    self.new_credential.delete_credential()
    self.assertEqual(len(Credentials.credentials_list), 1)
  
  # def test_generate_password(self):
  #   self.test_credential = Credentials("Bree95", "gmail", "")
  #   self.test_credential.password = generate_password()
  #   self.assertEqual()
  
  


if __name__ == '__main__':
  unittest.main()