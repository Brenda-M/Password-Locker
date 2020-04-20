class User:
  """
  Class that generates new instances of users

  """
  users_list = []

  def __init__ (self, first_name, last_name, nick_name, password):
    self.first_name = first_name
    self.last_name = last_name
    self.nick_name = nick_name
    self.password = password
  
  def save_user(self):
    User.users_list.append(self)

  def delete_user(self):
    User.users_list.remove(self)

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
    

