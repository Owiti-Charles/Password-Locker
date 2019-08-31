#!/usr/bin/env python3.6
from passlock import User, Credentials

def function():
	print(" __    __   __  ")
	print("|  |  |  | |  | ")
	print("|  |__|  | |  | ")
	print("|   __   | |  | ")
	print("|  |  |  | |  | ")
	print("|__|  |__| |__| ")

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


def passlocker():
    print("Hello Welcome to your Accounts credentials store...\n 1.  Create New Account ----- CA \n 2.  Have An Account -------- LI \n 3.  Close ------------------ EX")
    short_code=input("").lower()
    if short_code == "ex":
        print("It was nice having you. Come back again.......Goodbye!")
    elif short_code == "ca":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        password = input("Password: ")
        save_user(create_new_user(username,password))
        print('\n')
if __name__ == '__main__':
    passlocker()