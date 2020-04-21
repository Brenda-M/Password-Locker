#!/usr/bin/env python
from user_credentials import User, Credentials
import pyperclip
import string
import random

def create_user(username, password):
  '''
  Creates a new user account

  '''
  new_user = User(username, password)
  return new_user

def save_user(user):
  '''
  Saves a user account

  '''
  user.save_user()

def verify_user(user_name, password):
  '''
  Ensures that a user has created an account before the can log in

  '''
  finding_user = User.find_user(user_name, password)
  return finding_user

def create_credential(user_name, account_name, password):
  '''
  Creates a new credential

  '''
  new_credential = Credentials(user_name, account_name, password)
  return new_credential

def save_credentials(credential):
  '''
  Saves a user's credentials

  '''
  Credentials.save_credentials(credential)

def del_credential(credential):
  '''
  Deletes a credential from the account

  '''
  Credentials.delete_credential(credential)

def display_credential():
  '''
  Displays the saved credentials

  '''
  return Credentials.display_credentials()

def find_account (account_name):
  '''
  Finds a saved credential by it account name

  '''
  return Credentials.find_by_account_name(account_name)

def copy_credential(account_name):
  '''
  Copies a credentials password to the clipboard

  '''
  return Credentials.copy_credentials(account_name)

def generate_password(length):
  '''
  Generates a random password for the user

  '''
  letters = string.ascii_letters + string.digits 
  return ''.join((random.choice(letters)) for i in range(length))

def main(): 
  print('')
  print("Hello There! Welcome to the password vault")
  while True:
    print('-' * 70)
    print("Use these short codes to navigate through the vault: \n ca - To create an account \n li - To log In \n ex - To Exit")
    short_code = input("Enter code here: ").lower()

    print('')
    print('-' * 70)

    if short_code == 'ca':
      print("To create a new account: ")
      user_name = input ("Enter a username: ")
      password = input ("Create a password: ")
      save_user(create_user(user_name, password))
      print('')
      print('-' * 70)
      print(f"Thank you for joining us {user_name}")
      print(f"The password to your account is {password}. \nYou can log in to your account below") 

    elif short_code == 'li':
      print("Great to see you again.\nEnter your username and password below in order to log in")
      print('')
      user_name = input("Username: ").lower()
      password = str(input("Password: "))
      user_exists = verify_user(user_name, password)
      
      if user_exists == user_name:
        print('-' * 70)
        print(f"Welcome {user_name}, \nChoose one of the options below to proceed")
        print('')
        
        while True:
          print("cc - To add a credential \ndc - To display credentials \ndel - To delete a credential \nc - To copy a password \nex - To exit")    
          short_code = input ("Enter code: ").lower()

          print('-' * 70)

          if short_code == "cc":

            print("Enter your credentials below")
            account_name = input("Name of site: ").lower()
            user_name = input ("Username: ").lower()
            while True:
              print("Enter: \n op to create your own custom password, \n gp to generate one \n ex to exit")
              password_choice = input().lower()

              if password_choice == "op":
                password = input("Enter a password: ")
                break
              elif password_choice == "gp":
                password = generate_password(8)
                break
              elif password_choice == "ex":
                break
              else:
                print('-' * 70)
                print("The code you have entered does not exist. Please try again")
                print('-' * 70)

            save_credentials(create_credential(user_name, account_name, password))
            print('')
            print('-'* 70)
            print(f"Your credentials have been saved succesfully. \nAccount Name: {account_name} \nUserName: {user_name}. \nPassword: {password}")
            print('')
            print('-'* 70)

          elif short_code == 'del':
            print('-' * 70)
            delete_account = input("Enter the name of the account whose credentials you would like to delete, e.g Twiter: ").lower()
            del_credential(find_account(delete_account))
            print('')
            print('Credentials deleted succesfully')
            print('-' * 70)

          elif short_code == 'dc':
            if display_credential():
              print('=' * 70)
              print("Here is a list of all your credentials")
              print('')
              for user in display_credential():
                print(f'Account Name: {user.account_name}  UserName: {user.user_name}  Password: {user.password}')
              print('')
              print('=' * 70)
            else:
              print('-' * 70)
              print("There are no saved credentials")
              print('-' * 70)

          elif short_code == "c":
            choose_site = input("Enter the name of the site whose password you would like to copy: ").lower()
            copy_credential(choose_site)
            print('')
            print("Password copied succesfully")
            print('=' * 70)

          elif short_code == "ex":
            print("You have been logged out. Goodbye!!")
            break
          else:
            print('-' * 70)
            print("Please check your short code and try again")
            print('-' * 70)

      else:
        print('')
        print("Invalid login credentials. Check your username and password and then try again")
    elif short_code == "ex":
      print("We are sorry to see you leave. Goodbye!!")
      break
    else:
      print('-' * 70)
      print("Please check your short code and try again")
      print('-' * 70)

if __name__ == '__main__':
	main()

