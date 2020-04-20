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
    print("Use these short codes to navigate through the vault: \n ca - To create an account \n li - To log In \n ex - To Exit")
    short_code = input("Enter your option here: ").lower()

    if short_code == 'ca':
      print("To create a new account: ")
      first_name = input ("Enter your first name: ")
      last_name = input ("Enter your last name: ")
      nick_name = input ("Enter a nickname: ")
      password = input (" Enter your password: ")

      save_users(create_user(first_name, last_name, nick_name, password))
      print('\n')
      print(f"Thank you for joining us {first_name} {last_name}")
      print(f"Your username and password are {nick_name} and {password} respectively")
    
    elif short_code == 'li':
      print("We are glad that you are here. \n Enter your details below to log in to your account")
      nick_name = input("Nickname: ")
      password = str(input("Password: "))
      
      # if user_exists == nick_name:
      #   print(f"Welcome {nick_name}. \n Choose one of the options below to proceed")

      #   while True:
      #     print("cc - Add a credential \n dc- Display credentials \n c - Copy password \n ex - Exit")    
      #     short_code = input ("Enter code: ").lower()
      #     if short_code == "cc":
      #       print("Enter your credentials below")
      #       account_name = input("Name of site: ")
      #       user_name = input ("Username: ")

      #       while True:
      #         print("Enter op to create your own custom password and gp to generate one")
      #         password_choice == input().lower()

      #         if password_choice == "op":
      #           password = input("Enter a password: ")
      #           break
      #         elif password_choice == "gp":
      #           password = generate_password()
      #           break
          #     else:
          #       print("The code you have entered does not exist. Please try again")
      
          # elif short_code == "ex":
          #   print("You have been logged out. Goodbye!!")
          # else:
          #   print("Please check your short code and try again")

    # elif short_code == "ex":
    #   print("We are sorry to see you leave. Goodbye!!")
    #   break

    # else:
    #   print("Please check your short code and try again")
