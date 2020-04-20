import unittest
from users import User

class TestUsers(unittest.TestCase):
  """
  This is a test class that defines the test cases for the users class behavior

  """
  def setUp(self):
    '''
    set up method to run before each test case to ensure objects are being instantiated correctly
    '''
    self.new_user = User("Brenda", "Facebook", "4676jl")
  
  def test_init(self):
    self.assertEqual(self.new_user.user_name, "Brenda")
    self.assertEqual(self.new_user.account_name, "Facebook")
    self.assertEqual(self.new_user.password,"4676jl")
  
  if __name__ == '__main__':
    unittest.main()