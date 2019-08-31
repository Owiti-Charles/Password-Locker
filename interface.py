#!/usr/bin/env python3.6
from passlock import User, Credentials

def function():
	print("                          __    __   __  ")
	print("                         |  |  |  | |  | ")
	print("                         |  |__|  | |  | ")
	print("                         |   __   | |  | ")
	print("                         |  |  |  | |  | ")
	print("                         |__|  |__| |__| ")
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
def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_details()
def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()

def del_credential(credentials):
    """
    Function to delete a Credentials from credentials list

    """
    credentials.delete_credentials()

def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)
def check_credendtials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false

    """
    return Credentials.if_credential_exist(account)

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
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
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
        elif short_code == "dc":
            if display_accounts_details():
                print("Here's your list of acoount(s): ")
                 
                print('*' * 30)
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet..........")
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().capitalize()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "del":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().capitalize()
            if check_credendtials(search_name):
                search_credential = find_credential(search_name)
                print(f"{search_credential.account}")
                print("_"*30)
                credenttials.delete_credentials()
                print('\n')
                print(f"New Credential : {account} UserName: {user_Name}  successfully deleted!!!")
                print('\n')
            else:
                print("That Credential does not exist")
    else:
        print("Please enter a valid input to continue")

if __name__ == '__main__':
    passlocker()