# Password-Locker
## Author

[Owiti-Charles](https://github.com/Owiti-Charles)

## Description

This project is a python application that manages login and signup credentials of a person for various accounts i.e. username and passwords for each account. It also stores the passwords and generates a unique password for a user if they do not want to generate new passwords by themselves.

## Screenshot

<img src="https://raw.githubusercontent.com/Owiti-Charles/Password-Locker/master/images/ip1.png" width="900px" height="440px">

## User Stories
The user would like to.... :
* To create an account for the application or log into the application.
* Store my existing acounts login details for various accounts that i have registered for.
* Generate new password for an account that i haven't registered for and store it with the account name.   
* Delete stored account login details that i do now want anymore.
* Copy my credentials to the clipboard


## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3.6
* pyperclip
* pip

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ```https://github.com/Owiti-Charles/Password-Locker.git```

* cd Password-Locker

* code . or atom . based on the text editor you have.

### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:

        $ chmod +x interface.py
        $ ./interface.py
* To run test for the application
        $ python3 passlock_test.py

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./interface.py```|Hello Welcome to your Accounts Password Store... <br>* CA ---  Create New Account * LI ---  Have An Account |
|Select  CA| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select LI  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CC```|Enter Account, username, password<br>choose ```tp``` to enter your password or ```gp``` for the application to generate a password for you |
|Display all stored credentials | Enter ```DC```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```FC```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```D```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```D```| The application exits|

## Technologies Used

* python3.6

## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [mikeycharlesm7@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2019 **Owiti Charles**
