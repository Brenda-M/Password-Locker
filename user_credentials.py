import random
import string
import pyperclip

class User:
  """
  Class that generates new instances of users

  """
  users_list = []

  def __init__ (self, user_name, password):
    self.user_name = user_name
    self.password = password
  
  def save_user(self):
    User.users_list.append(self)

  def delete_user(self):
    User.users_list.remove(self)
  
  @classmethod
  def user_exists(cls, user_name):
    for user in cls.users_list:
      if user == user_name:
        return True
      return False


class Credentials:
  '''
  Class that generates account credentials and passwords.

  '''
  credentials_list = []

  def __init__(self, user_name, account_name, password):
    '''
    '''
    self.user_name = user_name
    self.account_name = account_name
    self.password = password
  
  def save_credentials(self):
    Credentials.credentials_list.append(self)
  
  def delete_credential(self):
    Credentials.credentials_list.remove(self)
  
  def generate_password(self, size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
    generated_password = ''.join(random.choice(chars) for _ in range(size))
    return generated_password
  
  @classmethod
  def display_credentials(cls, user_name):
    for credential in cls.credentials_list:
      print(credential)
  
  @classmethod
  def find_by_account_name(cls, account_name):
    for credential in cls.credentials_list:
      if credential.account_name == account_name:
        return credential
  
  @classmethod
  def copy_credentials(cls, account_name):
    copy_credential = Credentials.find_by_account_name(account_name)
    return pyperclip.copy(copy_credential.password)

    

