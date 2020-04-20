#/usr/bin/env python

from user_credentials import User

def create_user(fname, lname, nname, password):
  new_user = User(fname, lname, nname, password)
  return new_user

def save_users(user):
  user.save_user()

def del_user(user):
  user.delete_user()

def main(): 

  print("Hello There! Welcome to the password vault")

  while True:
    print("Use these short codes to navigate through the vault: \n ca - To create an account \n l - To log In \n ex - To Exit")
    short_code = input("Enter your option here: ").lower()

    if short_code == 'ca':
      print("To create a new account: ")
      first_name = input ("Enter your first name: ")
      last_name = input ("Enter your last name: ")
      nick_name = input ("Enter a nickname: ")
      password = input (" Enter your password: ")

      save_users(create_user(first_name, last_name, nick_name, password))
      print('\n')
      print(f"New account created for {first_name} {last_name}")
      print(f "Your password is {password}")