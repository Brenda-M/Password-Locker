import unittest
from user_credentials import User

class TestUsers(unittest.TestCase):
  """
  This is a test class that defines the test cases for the users class behavior

  Args:
	    unittest.TestCase: helps in creating test cases
  """
  def setUp(self):
    '''
    Method that runs before each test case to ensure objects are being instantiated correctly
    '''
    self.new_user = User("BMuthoni", "pass@word")
  
  def tearDown(self):
    User.users_list = []
  
  def test_init(self):
    self.assertEqual(self.new_user.user_name, "BMuthoni")
    self.assertEqual(self.new_user.password,"pass@word")
  
  def test_save_user(self):
    '''
    Test case to confirm that user objects are being saved to the user list
    '''
    self.new_user.save_user() #saving a new user 
    self.assertEqual(len(User.users_list), 1)
  
  def test_delete_user(self):
    '''
    Test to check whether a user can remove their account
    
    '''
    self.new_user.save_user()
    test_user = User("BMuthoni", "4676jl")
    test_user.save_user()
    self.new_user.delete_user()
    self.assertEqual(len(User.users_list), 1)
    
  def test_find_user(self):
    '''
    Test case to check test whether a user can only login once they have created an account

		'''
    self.new_user.save_user()
    test_user = User("Muthoni", "pass@word")
    test_user.save_user()
    for user in User.users_list:
      if user.user_name == test_user.user_name and user.password == test_user.password:
        current_user = user.user_name
        return current_user
    self.assertEqual(current_user, User.find_user(test_user.password, test_user.user_name))

  
if __name__ == '__main__':
  unittest.main()