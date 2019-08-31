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
    """
    function that checks whether a user exist and then login the user in.
    """
  
    check_user = Credentials.verify_user(username,password)
    return check_user

def create_new_credential(account,userName,password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account,userName,password)
    return new_credential
def save_credentials(lock):
    """
    Function to save Credentials
    """
    lock.save_account()
 
def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credentials.generatePassword()
    return auto_password


def passlocker():
    print("Hello Welcome to your Accounts credentials store...\n 1.  Create New Account ----- CA \n 2.  Have An Account -------- LI \n")
    short_code=input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        password = input("Password: ")
        save_user(create_new_user(username,password))
        print("*"*50)
        print(f"Hello {username}, Your account has been created succesfully!")
        print('\n')
    elif short_code == "li":
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
        print("Use these short codes:\n CC - Create a new credential , DC - Display Credentials,\n FC - Find a credential,\n EX - Exit the application,\n GP - Generate A randomn password,\n D - Delete credential")
        short_code = input().lower().strip()
        if short_code == 'cc':
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().capitalize()
            print("Your Account username")
            user_Name = input()
            while True:
                print(" TP - To type your own pasword:\n GP - To generate random Password")
                password_Choice = input("Enter").lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Password")
                    break
                elif password_Choice == 'gp':
                    password = generate_Password()
                    break
                elif password_Choice != 'tp' or 'gp':
                    print("Invalid password please try again")
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credential(account,user_Name,password))
            print('\n')
            print(f"New Credential : {account} UserName: {user_Name} Password:{password} created")
            print('\n')
    else:
        print("Please enter a valid input to continue")



if __name__ == '__main__':
    passlocker()