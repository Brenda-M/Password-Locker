#/usr/bin/env python

import pyperclip
from user_credentials import User, Credentials

def create_user(username, password):
  new_user = User(username, password)
  return new_user

def save_user(user):
  user.save_user()

def del_user(user):
  user.delete_user()

def verify_user(user_name, password):
  finding_user = Credentials.find_user(user_name, password)
  return finding_user

def create_credential(user_name, account_name, password):
  new_credential = Credentials(user_name, account_name, password)
  return new_credential

def save_credentials(credential):
  Credentials.save_credentials(credential)

def display_credential(user_name):
  return Credentials.display_credentials(user_name)

def copy_credential(account_name):
  return Credentials.copy_credentials(account_name)

def generate_password():
  gen_password = Credentials.generate_password()
  return gen_password

def main(): 

  print("Hello There! Welcome to the password vault")

  while True:
    print("Use these short codes to navigate through the vault: \n ca - To create an account \n li - To log In \n ex - To Exit")
    short_code = input("Enter your option here: ").lower()

    if short_code == 'ca':
      print("To create a new account: ")
      user_name = input ("Enter a username: ")
      password = input (" Create a password: ")
      save_user(create_user(user_name, password))
      print('\n')
      print(f"Thank you for joining us {user_name}")
      print(f"The password to your account is {password}") 
    elif short_code == 'li':
      print("We are glad that you are here. \n Enter your details below to log in to your account")
      user_name = input("Username: ")
      password = str(input("Password: "))
      user_exists = verify_user(user_name, password)
      
      if user_exists == user_name:
        print(f"Welcome {user_name}. \n Choose one of the options below to proceed")
        while True:
          print("cc - Add a credential \n dc- Display credentials \n c - Copy password \n ex - Exit")    
          short_code = input ("Enter code: ").lower()
          if short_code == "cc":
            print("Enter your credentials below")
            account_name = input("Name of site: ")
            user_name = input ("Username: ")
            while True:
              print("Enter: \n op to create your own custom password, \n gp to generate one \n ex to exit")
              password_choice = input().lower()
              if password_choice == "op":
                password = input("Enter a password: ")
                break
              elif password_choice == "gp":
                password = generate_password()
                break
              elif password_choice == "ex":
                break
              else:
                print("The code you have entered does not exist. Please try again")
            save_credentials(create_credential(user_name, account_name, password))
            print(f"Your credentials have been saved succesfully. Account Name: {account_name} UserName: {user_name}. Password: {password}")
          elif short_code == 'dc':
            if display_credential(user_name):
              print("Here is a list of all your credentials")
              for credential in display_credential(user_name):
                print(f'Account Name: {credential.account_name} - UserName: {credential.user_name} - Password: {credential.password}')
            else:
              print("You have not any saved credentials yet")
          elif short_code == "c":
            choose_site = input("Enter name of site you want to copy")
            copy_credential(choose_site)
          elif short_code == "ex":
            print("You have been logged out. Goodbye!!")
          else:
            print("Please check your short code and try again")
    elif short_code == "ex":
      print("We are sorry to see you leave. Goodbye!!")
      break
    else:
      print("Please check your short code and try again")

if __name__ == '__main__':
	main()

