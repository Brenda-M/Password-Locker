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
    self.new_user = User("BMuthoni", "4676jl")
  
  def tearDown(self):
    User.users_list = []
  
  def test_init(self):
    self.assertEqual(self.new_user.user_name, "BMuthoni")
    self.assertEqual(self.new_user.password,"4676jl")
  
  def test_save_user(self):
    '''
    Test case to confirm that user objects are being saved to the user list
    '''
    self.new_user.save_user() #saving a new user 
    self.assertEqual(len(User.users_list), 1)
  
  def test_delete_user(self):
    self.new_user.save_user()
    test_user = User("BMuthoni", "4676jl")
    test_user.save_user()
    self.new_user.delete_user()
    self.assertEqual(len(User.users_list), 1)
  
  def test_user_exists(self):
    self.new_user.save_user()
    test_user = User("BMuthoni", "4676jl")
    test_user.save_user()
    user_exist = User.user_exists("BMuthoni")
    self.assertTrue(user_exist)

  
if __name__ == '__main__':
  unittest.main()