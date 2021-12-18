import json
# Used to write the dictionary data to the txt file https://www.geeksforgeeks.org/write-a-dictionary-to-a-file-in-python/ can be found here
from json.decoder import JSONDecodeError
import os  # Used to handle files
from random import randint  # Used to generate account numbers
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' #Regular expression for validating user email

username = ''  # Global variable to store username


def acc_no_gen():
    """
    Function used to generate the account number, this is done by using a range of n values and choosing a random number from them
    """
    range_start = 5**(5-1)
    range_end = (5**5)-1
    num = randint(range_start, range_end)
    return num


def user():
    #Prints gui menu to the user
    print("*************************************")
    print("=<< 1. Create new bank account    >>=")
    print("=<< 2. Check Account Details      >>=")
    print("=<< 3. Delete Account             >>=")
    print("=<< 4. Withdraw                   >>=")
    print("=<< 5. Deposit                    >>=")
    print("=<< 6. Transfer                   >>=")
    print("=<< 7. Exit                       >>=")
    print("*************************************")
    choice = input(f'Select your choice number from the above menu:\n')
    if choice == "1":
        print("*************************************")
        print("=<< 1. Create Checking Account    >>=")
        print("=<< 2. Check Savings  Account     >>=")
        print("=<< 3. Exit                       >>=")
        print("*************************************")
        acc_choice = input(f'Select your choice number from the above menu:\n')
        if acc_choice == "1":
            createChecking()
            user()
        elif acc_choice == "2":
            createSavings()
            user()
        elif acc_choice == "3":
            user()
        else:
            print('Incorrect input')
            user()
    elif choice == "2":
        account()
    elif choice == "3":
        delete()
    elif choice == "4":
        withdraw()
    elif choice == "5":
        deposit()
    elif choice == "6":
        transfer()
    elif choice == "7":
        welcome()
    else:
        print('Wrong input')
        user()


def createSavings():
    """
    Funciton call used to generate a savings account. This works by passing the blank account information to the savings account class.
    
    The create account function is then called from within that class, finally the user function is prompted again to return our user to the main menu
    """
    account = SavingsAccount(0, '', 0, '')
    account.createSavingsAccount()
    user()


def createChecking():
    """
    Funciton call used to generate a Checking account. This works by passing the blank account information to the checking account class.
    
    The create account function is then called from within that class, finally the user function is prompted again to return our user to the main menu
    """
    account = CheckingAccount(0, '', 0, '')
    account.createCheckingAccount()
    user()


def account():
    """
    Function used to return account balence, it also includes general error checking against incorrect input and missing account numbers.
    """
    try:
        #Open the customer file as a json file in read+ mode
        with open("customer.txt", "r+") as jFile:
            #Assign the loaded json file to jObject var
            jObject = json.load(jFile)

        #Variable to store user input
        var = input("Enter account number:")

        #Finds the result from within the dictionary jObject
        result = jObject[var]["Account Balance"]

        #Prints out our account details
        print(f"Account balance is: {result}")

    #Should a value other than an int be passed display an error message
    except ValueError:
        print('Only integers are allowed')
        user()

    #Should an account not be in the system display an error message
    except KeyError:
        print("Account does not exist")
        user()


def exit():
    #Print out exit message and exit program
    print("Thank you for using our banking system!")


def login():
    """
    Function that facilitates user login and error checking
    """
    print("         ------Login------           ")
    print("*************************************")

    #Takes user input for username and password
    username = input("Please enter your username:\n")
    password = input(f'Please enter your password:\n')

    #Opens user file in read mode
    with open('user.txt', "r") as jFile:
        #Load the file as a json and assign it to jObject
        jObject = json.load(jFile)

    try:
        #Conditional statement to check if user login matches stored username and password
        if jObject[username]["Username"] == username and jObject[username]["Password"] == password:
            #If the username and password match the ones stored print welcome message and direct the user to the user function
           print(f"Welcome {username}")
           user()
        else:
            #If the password does not match print error
            print("Password was incorrect!")
            #Return user to login function
            login()
    except KeyError:
        #If the username does not exist in the database print appropriate error
        print("Username was incorrect!")
        #Return user to login function
        login()


def register():
    """
    Function to register a new user to our stored user file
    """

    #Enter user details
    print(f"Enter Details")
    username = input(f"Please enter your username:\n")
    #Ensures the inputted username is at least 5 characters long
    if len(username) < 5:
        print("Username must be at least 5 characters long")
        register()
    password = input(f'Please enter your password:\n')
    #Ensures the inputted password is at least 7 characters long
    if len(password) < 7:
        print("Password must be at least 7 characters long")
        register()
        
    name = input(f'Please enter your full name:\n')
    
    #Ensure email inputted is valid using a regex expression
    email = input(f'Please enter your email:\n')
    #If email is valid print success message and direct user to the login page
    if(re.fullmatch(regex, email)):
        print("Account creation successful!\n")
        print("Proceed to login\n")
    else:
        print("Enter a valid email")
        register()
    
   
    

   #Store all user input in a dictionarys
    register_input = {
        username:
            {
                "Username": username,
                "Password": password,
                "Email": email,
                "Full Name": name,
            },
    }

    #If the user file is empty execute loop
    if os.stat('user.txt').st_size == 0:
        #Open the user file in read+
        with open('user.txt', "r+") as jFile:
            #Write the json data to the empty file
            # Indent beautifies output
            json.dump(register_input, jFile, indent=2)
    #Else if the file contains data
    else:
        #Load the file in read+
        with open('user.txt', "r+") as jFile:
            #Assign jObject to loaded data
            jObject = json.load(jFile)
            #Append the user data to jObject
            jObject.update(register_input)
            #Seek to the start of the file
            jFile.seek(0)
            #Overwrite old data with updated data
            json.dump(jObject, jFile, indent=2)
    #Direct user to login function
    login()


def welcome():
    """
    Function to print welcome menu to user
    """
    print("=====================================")
    print("     ----Welcome to Bank----       ")
    print("*************************************")
    print("=<< 1. Login:                 >>=")
    print("=<< 2. Register:              >>=")
    print("=<< 3. Exit:                  >>=")
    print("*************************************")
    choice = input(f'Select your choice number from the above menu:\n')
    if choice == "1":
        login()
    elif choice == "2":
        register()
    elif choice == "3":
        exit()
    else:
        print('Wrong input')
        welcome()


def delete():
    """
    Function to delete (close) a bank account
    """
    try:
        #User input for account they wish to close
        var = input("Enter account number you wish to close:\n")
    except ValueError:
        #If number enterred is not an int return an error
        print("Enter a valid account number!")
        #Direct user back to withdraw function
        delete()
        

    try:
        #Opens user file in read+
        with open("customer.txt", "r+") as jFile:
            #Assign loaded data to jObject variable
            jObject = json.load(jFile)
            #Seek to desired key and delete it
            del(jObject[var])
            #Seek to beginning of the file
            jFile.seek(0)
            #Rewrite file with correct data
            json.dump(jObject, jFile, indent=2)
            #Truncate new file
            jFile.truncate()
    except KeyError:
        #If the username does not exist in the database print appropriate error
        print("Account no was incorrect!")

    #Direct user back to the user menu
    user()


def withdraw():
    """
    Function to withdraw money from a specific account
    """
    try:
        #User inputs account they want to access
        var = int(input("Enter account number you wish to withdraw from:\n"))
    except ValueError:
        #If number enterred is not an int return an error
        print("Enter a valid account number!")
        #Direct user back to withdraw function
        withdraw()
        
    try:
        #User input for amount they wish to withdraw
        amount = int(input("Enter amount you with to withdraw: (Must be a whole number)\n"))
    except ValueError:
        #If amount enterred is not an int return an error
        print("Amount must be a whole number!")
        #Direct user back to withdraw function
        withdraw()
   
    try:
         #Opens user file in read+
        with open("customer.txt", "r+") as jFile:
            #Assign loaded data to jObject variable
            jObject = json.load(jFile)
            #Seek to inputted key and decrement the account balance variable by desired amount
            jObject[var]["Account Balance"] -= amount
            #Seek to beginning of the file
            jFile.seek(0)
            #Rewrite file with correct data
            json.dump(jObject, jFile, indent=2)
            #Truncate new file
            jFile.truncate()
    except KeyError:
        #If the username does not exist in the database print appropriate error
        print("Account no was incorrect!")
    #Direct user back to the user menu
    user()


def deposit():
    """
    Function to deposit money to a specific account
    """
    try:
        #User inputs account they want to access
        var = input("Enter account number you wish to deposit into:\n")
    except ValueError:
        #If number enterred is not an int return an error
        print("Enter a valid account number!")
        #Direct user back to deposit function
        deposit()
    try:
        #User input for amount they wish to deposit
        amount = int(input("Enter amount you with to deposit: (Must be a whole number)\n"))
    except ValueError:
        #If amount enterred is not an int return an error
        print("Amount must be a whole number!")
        #Direct user back to deposit function
        deposit()
    
    try:    
        #Opens user file in read+
        with open("customer.txt", "r+") as jFile:
            #Assign loaded data to jObject variable
            jObject = json.load(jFile)
            #Seek to inputted key and increment the account balance variable by desired amount
            jObject[var]["Account Balance"] += amount
            #Seek to beginning of the file
            jFile.seek(0)
            #Rewrite file with correct data
            json.dump(jObject, jFile, indent=2)
            #Truncate new file
            jFile.truncate()
    except KeyError:
        #If the username does not exist in the database print appropriate error
        print("Account no was incorrect!")
    #Direct user back to the user menu
    user()


def transfer():
    """
    Function to transfer money between accounts
    """
    #User inputs account they want to access
    var1 = input("Enter account number you wish to transfer from:\n")
    #User inputs account they want to transfer to
    var2 = input("Enter account number you wish to transfer to:\n")
    #User input for amount they wish to transfer
    amount = int(input("Enter amount you with to transfer:\n"))
    #Opens user file in read+
    with open("customer.txt", "r+") as jFile:
        #Assign loaded data to jObject variable
        jObject = json.load(jFile)
        #Seek to inputted key and decrement the account balance variable by desired amount
        jObject[var1]["Account Balance"] -= amount
        #Seek to inputted key and increment the account balance variable by desired amount
        jObject[var2]["Account Balance"] += amount
        #Seek to beginning of the file
        jFile.seek(0)
        #Rewrite file with correct data
        json.dump(jObject, jFile, indent=2)
        #Truncate new file
        jFile.truncate()
    #Direct user back to the user menu
    user()


class Account(object):
    """
    Account definition for general account attributes
    """
    def __init__(self, acc_no, name, balance, acc_type, transactions=None):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = 0
        if transactions is None:
            self.transactions = []
        else:
            self.transactions = transactions

    # def __str__(self):
    #     result = "Account Name: " + self.name + "\n"
    #     result += "Account number: " + str(self.acc_no) + "\n"
    #     result += "Account Balance: " + str(self.balance) + "\n"

   
    #    return result


class SavingsAccount(Account):
    """
    Savings account class definition and functions
    """
    #Inherit Account class variables
    def __init__(self, acc_no, name, balance, acc_type, transactions=None):
        super().__init__(acc_no, name, balance, acc_type, transactions=transactions)

    #Function to create a new savings account
    def createSavingsAccount(self):
        #Get age input from user
        age_chk = int(input("Enter your age:"))
        #If input is less that the minimum account age print an error message
        if age_chk < 14:
            print("User too young for selected account type!")
            user()
        #Otherwise allow the user to create an account
        else:
            #Assign result of acc_no_gen funtion to the acc no variable
            self.acc_no = acc_no_gen()
            #User input for name
            self.name = input("Enter the account holder name:")
            #User input for opening balance
            try:
                self.balance = int(input("Enter The Initial deposit: (Must be a whole number)"))
            except ValueError:
                print("Deposit must be a whole number!")
                user()
            self.acc_type = "Savings"
            
            #Dictionary storing customer data
            customer_input_data = {
                self.acc_no:
                    {
                        'Account Number': self.acc_no,
                        'Account Name': self.name.title(),
                        'Account Balance': self.balance,
                        'Account Type': self.acc_type
                    },
            }
            #Display success message
            print(f"An account with account number {self.acc_no} has been opened for {self.name}")
            
            #If the customer file is empty execute loop
            if os.stat('customer.txt').st_size == 0:
                #Open the customer file in read+
                with open('customer.txt', 'r+') as jFile:
                    #Write the json data to the empty file
                    json.dump(customer_input_data, jFile, indent=2)
            #Else if the file contains data
            else:
                #Load the file in read+
                with open('customer.txt', "r+") as jFile:
                    #Assign jObject to loaded data
                    jObject = json.load(jFile)
                    #Append the customer data to jObject
                    jObject.update(customer_input_data)
                    #Seek to the start of the file
                    jFile.seek(0)
                    #Overwrite old data with updated data
                    json.dump(jObject, jFile, indent=2)


class CheckingAccount(Account):
    """
    Checking account class definition and functions
    """
    #Inherit Account class variables
    def __init__(self, acc_no, name, balance, acc_type, transactions=None):
        super().__init__(acc_no, name, balance, acc_type, transactions=transactions)

    #Function to create a new current account
    def createCheckingAccount(self):
        #Get age input from user
        age_chk = int(input("Enter your age:"))
        #If input is less that the minimum account age print an error message
        if age_chk < 18:
            print("User too young for selected account type!")
            user()
        #Otherwise allow the user to create an account
        else:
            #Assign result of acc_no_gen funtion to the acc no variable
            self.acc_no = acc_no_gen()
            #User input for name
            self.name = input("Enter the account holder name: ")
            #User input for opening balance
            try:
                self.balance = int(input("Enter The Initial deposit: (Must be a whole number)"))
            except ValueError:
                print("Deposit must be a whole number!")
                user()
            self.acc_type = "Checking"

            #Dictionary storing customer data
            customer_input_data = {
                self.acc_no:
                {
                    'Account Number': self.acc_no,
                    'Account Name': self.name.title(),
                    'Account Balance': self.balance,
                    'Account Type': self.acc_type
                },
            }

            #Display success message
            print(f"An account with account number {self.acc_no} has been opened for {self.name}")
            
            #If the customer file is empty execute loop
            if os.stat('customer.txt').st_size == 0:
                #Open the customer file in read+
                with open('customer.txt', 'r+') as jFile:
                    #Write the json data to the empty file
                    json.dump(customer_input_data, jFile, indent=2)
            #Else if the file contains data
            else:
                #Load the file in read+
                with open('customer.txt', "r+") as jFile:
                    #Assign jObject to loaded data
                    data = json.load(jFile)
                    #Append the customer data to jObject
                    data.update(customer_input_data)
                    #Seek to the start of the file
                    jFile.seek(0)
                    #Overwrite old data with updated data
                    json.dump(data, jFile, indent=2)


welcome()


"""
with open("user.txt") as jFile:
    jObject = json.load(jFile)
    jFile.close()
with open("customer.txt") as jFile:
    jObject = json.load(jFile)
    jFile.close()
var = input("Acc No")
testUser = jObject[var]['Account Name']
print(testUser)
sean = jObject["2"]
print(sean)
acc = Account(123,"testacc", 250, "Savings")
print(acc)
"""