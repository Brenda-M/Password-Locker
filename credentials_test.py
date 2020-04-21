import unittest
import pyperclip
from user_credentials import Credentials

class TestCredentials(unittest.TestCase):

  def setUp(self):
    self.new_credential = Credentials("Bree95", "Facebook", "password1")

  def tearDown(self):
    Credentials.credentials_list = []

  def test_init(self):
    '''
    Test case to test if the object is initialized properly

    '''
    self.assertEqual(self.new_credential.user_name, "Bree95")
    self.assertEqual(self.new_credential.account_name, "Facebook")
    self.assertEqual(self.new_credential.password, "password1")

  def test_save_credentials(self):
    '''
    Test case to test if the credentials object is saved into the credentials list

    '''
    self.new_credential.save_credentials()
    self.assertEqual(len(Credentials.credentials_list), 1)
  
  def test_save_multiple_credentials(self):
    '''
    Test case to check is we can save multiple credentials objects to the credentials_list

    '''
    self.new_credential.save_credentials()
    test_credential = Credentials("Brenda", "gmail", "4676jl")
    test_credential.save_credentials()
    self.assertEqual(len(Credentials.credentials_list), 2)

  def test_delete_credentials(self):
    '''
    Test case to test if user can remove credential from credentials list.
    
    '''
    self.new_credential.save_credentials()
    test_credential = Credentials("Brenda", "gmail", "4676jl")
    test_credential.save_credentials()
    self.new_credential.delete_credential()
    self.assertEqual(len(Credentials.credentials_list), 1)
  
  def test_find_by_account_name(self):
    '''
    Test to check whether we can find a credential by its name and display information

    '''
    self.new_credential.save_credentials()
    test_credential = Credentials('Brenda', 'gmail', '4676jl' )
    test_credential.save_credentials()
    found_credential = Credentials.find_by_account_name('gmail')
    self.assertEqual(found_credential.account_name, test_credential.account_name)

  def test_copy_credential(self):
    '''
    Test to check if user can copy the right credentials
    
    '''
    self.new_credential.save_credentials()
    test_credential = Credentials('Brenda', 'gmail', '4676jl' )
    test_credential.save_credentials()
    find_credential = None
    for credential in Credentials.credentials_list:
        find_credential = Credentials.find_by_account_name(credential.account_name)
        return pyperclip.copy(find_credential.password)
    self.assertEqual('4676jl', pyperclip.paste())
    print(pyperclip.paste())
    
if __name__ == '__main__':
  unittest.main()