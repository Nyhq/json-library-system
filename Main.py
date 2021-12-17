import json  # Used to write the dictionary data to the txt file https://www.geeksforgeeks.org/write-a-dictionary-to-a-file-in-python/ can be found here
import os
from random import randint

username = ''


def acc_no_gen():
    range_start = 4**(4-1)
    range_end = (4**4)-1
    num = randint(range_start, range_end)
    return num


def user():
    print("*************************************")
    print("=<< 1. Create new bank account    >>=")
    print("=<< 2. Check Account Details      >>=")
    print("=<< 3. Delete Account             >>=")
    print("=<< 3. Exit             >>=")
    print("*************************************")
    choice = input(f'Select your choice number from the above menu:\n')
    if choice == "1":
        print("*************************************")
        print("=<< 1. Create Checking Account    >>=")
        print("=<< 2. Check Savings  Account    >>=")
        print("=<< 3. Exit                     >>=")
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
        test()
        #delete_account()
    elif choice == "4":
        welcome()
    else:
        print('Wrong input')
        user()


def createSavings():
    account = SavingsAccount(0, '', 0, '')
    account.createSavingsAccount()
    user()


def createChecking():
    account = CheckingAccount(0, '', 0, '')
    account.createCheckingAccount()
    user()


def account():
    try:
        acc_num_input = int(input(f"\nEnter customer's account number:"))
        with open('customer.txt') as cust_file:
            data = json.load(cust_file)
            found_flag = False
        for user_data in data:
            for user_data_key in user_data.keys():
                for user_details in user_data[user_data_key]:
                    if acc_num_input in user_details.values():
                        found_flag = True
                        print('\nAccount Found ! See details below:')
                        print(user_details)
                        user()
        if found_flag == False:
            print('\nAccount Not Found! You can register a new one if you wish.\n')
            user()
    except ValueError:
        print('Only integers are allowed')
        user()


def exit():
    file = open('customer.txt', 'r+')
    file.truncate()
    file.close()
    print("Thank you for using our banking system!")


def login():
    print(f"Enter Details")
    username = input("Please enter your username:\n")
    password = input(f'Please enter your password:\n')
    with open('user.txt') as json_file:
        data = json.load(json_file)
        while (username != (data['User 1']['Username']) or password != (data['User 1']['Password'])) and (username != (data['User 2']['Username']) or password != (data['User1 2']['Password'])):
            print('Username or password not found')
            login()
        else:
            print(f'Welcome {username}')
            user()


def welcome():
    print("=====================================")
    print("     ----Welcome to Bank----       ")
    print("*************************************")
    print("=<< 1. Login:                >>=")
    print("=<< 2. Exit:                  >>=")
    print("*************************************")
    choice = input(f'Select your choice number from the above menu:\n')
    if choice == "1":
        login()
    elif choice == "2":
        exit()
    else:
        print('Wrong input')
        welcome()

# def delete_account():
#     try:
#         acc_num_input = int(input(f"\nEnter customer's account number:"))
#         with open('customer.txt') as cust_file:
#             data = json.load(cust_file)
#             found_flag = False
#         for user_data in data:
#             for user_data_key in user_data.keys():
#                 for user_details in user_data[user_data_key]:
#                     if acc_num_input in user_details.values():
#                         found_flag = True
#                         print('\nAccount Found ! See details below:')
#                         del data.pop('test')
#                         user()
#         if found_flag == False:
#             print('\nAccount Not Found! You can register a new one if you wish.\n')
#             user()
#     except ValueError:
#         print('Only integers are allowed')
#         user()

def test():
    with open('customer.txt') as cust_file:
        data = json.load(cust_file)
 
        # Print the type of data variable
        print("Type:", type(data))

        accountID = data[0]["Test:Account Number"]
        print(accountID)
        # Print the data of dictionary
        # print("\nAcc1:", data["Test"][0])
        # print("\nAcc2:", data["Test2"][0])


class Account(object):
    def __init__(self, acc_no, name, balance, acc_type, transactions=None):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = 0
        if transactions is None:
            self.transactions = []
        else:
            self.transactions = transactions

    def __str__(self):
        result = "Account Name: " + self.name + "\n"
        result += "Account number: " + str(self.acc_no) + "\n"
        result += "Account Balance: " + str(self.balance) + "\n"

        last = len(self.transactions)
        first = last - 5
        if first < 0:
            first = 0

        if last == 0:
            return result

        result += "Transactions \n"
        for index in range(last, first, -1):
            result += "#" + str(index) + " acc_Type: " + self.transactions[index - 1][0] + ". Amount: " + str(
                self.transactions[index - 1][1]) + "\n"

        return result


class SavingsAccount(Account):
    def __init__(self, acc_no, name, balance, acc_type, transactions=None):
        super().__init__(acc_no, name, balance, acc_type, transactions=transactions)

    def createSavingsAccount(self):

        self.acc_no = acc_no_gen()
        self.name = input("Enter the account holder name: ")
        self.balance = int(input("Enter The Initial deposit:"))
        self.acc_type = "Savings"

        customer_file_data = []
        customer_banking_data = {
            self.acc_no: [
                {
                    'Account Number': self.acc_no,
                    'Account Name': self.name.title(),
                    'Opening Balance': self.balance,
                    'Account Type': self.acc_type
                }
            ],
        }
        print(
            f"An account with account number {self.acc_no} has been opened for {self.name}")
        if os.stat('customer.txt').st_size == 0:
            customer_file_data.append(customer_banking_data)
            with open('customer.txt', 'w') as obj:
                json.dump(customer_file_data, obj)
        else:
            with open('customer.txt') as obj:
                data = json.load(obj)
                data.append(customer_banking_data)
                with open('customer.txt', 'w') as obj:
                    json.dump(data, obj)
                    


class CheckingAccount(Account):
    def __init__(self, acc_no, name, balance, acc_type, transactions=None):
        super().__init__(acc_no, name, balance, acc_type, transactions=transactions)

    def createCheckingAccount(self):
        
        self.acc_no = acc_no_gen()
        self.name = input("Enter the account holder name: ")
        self.balance = int(input("Enter The Initial deposit:"))
        self.acc_type = "Checking"

        customer_file_data = []
        customer_banking_data = {
            self.acc_no: [
                {
                    self.name.title():
                    {
                        'Account Number': self.acc_no,
                        'Account Name': self.name.title(),
                        'Opening Balance': self.balance,
                        'Account Type': self.acc_type
                    }
                }
            ],
        }
        print(
            f"An account with account number {self.acc_no} has been opened for {self.name}")
        if os.stat('customer.txt').st_size == 0:
            customer_file_data.append(customer_banking_data)
            with open('customer.txt', 'w') as obj:
                json.dump(customer_file_data, obj)
        else:
            with open('customer.txt') as obj:
                data = json.load(obj)
                data.append(customer_banking_data)
                with open('customer.txt', 'w') as obj:
                    json.dump(data, obj)


welcome()
