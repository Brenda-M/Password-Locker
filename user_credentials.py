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
    '''
    save_user method saves user objects into users_list

    '''
    User.users_list.append(self)

  def delete_user(self):
    '''
    delete_user method removes a saved user from the users_list
    
    '''
    User.users_list.remove(self)
     
  @classmethod
  def find_user(cls, user_name, password):
    '''
    find_user method verifies whether a user has been saved in the users_list
    '''
    current_user = ''
    for user in User.users_list:
      if user.user_name == user_name and user.password == password:
        current_user = user.user_name
        return current_user
  
class Credentials:
  '''
  Class that generates account credentials and displays them.

  '''
  credentials_list = []
  user_credentials_list = []

  def __init__(self, user_name, account_name, password):
    self.user_name = user_name
    self.account_name = account_name
    self.password = password
  
  def save_credentials(self):
    '''
    save_credentials method saves a credential object into the credentials_list
    '''
    Credentials.credentials_list.append(self)
  
  def delete_credential(self):
    '''
    delete_credentials method removes a saved credential from the credentials_list
    '''
    Credentials.credentials_list.remove(self)
  
  @classmethod
  def find_by_user_name(cls, user_name):
    '''
    This method searches the credentials_list by user_name and appends the information to a new empty list
    '''
    user_credentials_list = []
    for credential in cls.credentials_list:
      if credential.user_name == user_name:
        user_credentials_list.append(credential)
        return user_credentials_list
				
  @classmethod
  def find_by_account_name(cls, account_name):
    '''
    This method finds a credential using its account_name

    '''
    for credential in cls.credentials_list:
      if credential.account_name == account_name:
        return credential
  
  @classmethod
  def copy_credentials(cls, account_name):
    '''
    This method allows the user to copy a credential's password
    '''
    copy_credential = Credentials.find_by_account_name(account_name)
    return pyperclip.copy(copy_credential.password)
  


    

