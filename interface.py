#!/usr/bin/env python3.6
from passlock import User, Credentials

def function():
	print("                                  __    __   __  ")
	print("                                 |  |  |  | |  | ")
	print("                                 |  |__|  | |  | ")
	print("                                 |   __   | |  | ")
	print("                                 |  |  |  | |  | ")
	print("                                 |__|  |__| |__| ")
function()

def create_new_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()
def display_user():
    """
    Function to display existing user
    """
    return User.display_user()
def login_user(username,password):
  
  #function that checks whether a user exist and then login the user in.
  
  check_user = Credentials.verify_user(username,password)
  return check_user


def passlocker():
    print("Hello Welcome to your Accounts credentials store...\n 1.  Create New Account ----- CA \n 2.  Have An Account -------- LI \n 3.  Close ------------------ EX")
    short_code=input("").lower().strip()
    if short_code == "ex":
        print("It was nice having you. Come back again another time.......Goodbye!")
    elif short_code == "ca":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        password = input("Password: ")
        save_user(create_new_user(username,password))
        print(f"Hello {username}, Your account has been created succesfully!")
        print("*"*50)
        print('\n')
    elif short_code == "li":
        print("Login! ")
        print("*"*50)
        print("Enter your User name and your Password to log in:")
        print('*' * 50)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To PassWord Locker Manager")  
            print('\n')
            print("what would you like to do?")
            print('\n')
    while True:
        print("Use these short codes : cc - Create a new credential, dc - Display Credential(s), fc - Find a credential,ex - Exit the application, gp- Generate A randomn password, del- Delete credential,cp-Copy Password")
        short_code = input().lower()



if __name__ == '__main__':
    passlocker()