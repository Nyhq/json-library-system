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
    account = SavingsAccount(0, '', 0, '')
    account.createSavingsAccount()
    user()

def createChecking():
    account = CheckingAccount(0, '', 0, '')
    account.createCheckingAccount()
    user()

def account():
    try:
        with open("customer.txt", "r+") as jFile:
            jObject = json.load(jFile)

        var = input("Enter account number:")
        
        result = jObject[var]
        
        print(result)
       
    except ValueError:
        print('Only integers are allowed')
        user()

def exit():
    print("Thank you for using our banking system!")

def login():
    print("         ------Login------           ")
    print("*************************************")
    username = input("Please enter your username:\n")
    password = input(f'Please enter your password:\n')
    with open('user.txt') as jFile:
        jObject = json.load(jFile)
        
    if jObject[username]["Username"] == username and jObject[username]["Password"] == password:
           print(f"Welcome {username}")
           user()
    else:
        print("Username or password was incorrect!")
        login()
        
def register():
    print(f"Enter Details")
    username = input("Please enter your username:\n")
    password = input(f'Please enter your password:\n')
    email = input(f'Please enter your email:\n')
    name = input(f'Please enter your full name:\n')
   
    register_input = {
        username:
            {
                "Username":username,
                "Password":password,
                "Email":email,
                "Full Name":name,
            },
    }
    if os.stat('user.txt').st_size == 0:
        with open('user.txt', "r+") as jFile:
            json.dump(register_input, jFile, indent = 2)
    else:   
        with open('user.txt', "r+") as jFile:
                    jObject = json.load(jFile)
                    jObject.update(register_input)
                    jFile.seek(0)
                    json.dump(jObject, jFile, indent = 2)
    login()
    
       

def welcome():
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
    var = input("=<< Enter account number you wish to close: >>=\n")
    with open("customer.txt", "r+") as jFile:
        jObject = json.load(jFile)
        del(jObject[var])
        jFile.seek(0)
        json.dump(jObject, jFile, indent = 2)
        jFile.truncate()
    
    user()
    # x = jObject.pop("188")
    
    # with open("customer.txt", "r+") as jFile:
    #   jObject = json.dump(jObject, jFile, indent = 2)
    # var = input("Please enter the account number that you wish to close:")
    # x = jObject.pop(var)

def withdraw():
    var = input("Enter account number you wish to withdraw from:\n")
    amount = int(input("Enter amount you with to withdraw:\n"))
    with open("customer.txt", "r+") as jFile:
        jObject = json.load(jFile)
        jObject[var]["Account Balance"] -= amount
        jFile.seek(0)
        json.dump(jObject, jFile, indent = 2)
        jFile.truncate()
    
    user()

def deposit():
    var = input("Enter account number you wish to deposit into:\n")
    amount = int(input("Enter amount you with to deposit:\n"))
    with open("customer.txt", "r+") as jFile:
        jObject = json.load(jFile)
        jObject[var]["Account Balance"] += amount
        jFile.seek(0)
        json.dump(jObject, jFile, indent = 2)
        jFile.truncate()
    
    user()

def balence():
    return

def transfer():
    var1 = input("Enter account number you wish to transfer from:\n")
    var2 = input("Enter account number you wish to transfer to:\n")
    amount = int(input("Enter amount you with to transfer:\n"))
    with open("customer.txt", "r+") as jFile:
        jObject = json.load(jFile)
        jObject[var1]["Account Balance"] -= amount
        jObject[var2]["Account Balance"] += amount
        jFile.seek(0)
        json.dump(jObject, jFile, indent = 2)
        jFile.truncate()
    
    user()

def selectAccount():
    acc_select = input("Enter account you wish to select:")

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

    # def __str__(self):
    #     result = "Account Name: " + self.name + "\n"
    #     result += "Account number: " + str(self.acc_no) + "\n"
    #     result += "Account Balance: " + str(self.balance) + "\n"

    #     last = len(self.transactions)
    #     first = last - 5
    #     if first < 0:
    #         first = 0

    #     if last == 0:
    #         return result

    #     result += "Transactions \n"
    #     for index in range(last, first, -1):
    #         result += "#" + str(index) + " acc_Type: " + self.transactions[index - 1][0] + ". Amount: " + str(
    #             self.transactions[index - 1][1]) + "\n"

    #    return result


class SavingsAccount(Account):
    def __init__(self, acc_no, name, balance, acc_type, transactions=None):
        super().__init__(acc_no, name, balance, acc_type, transactions=transactions)

    def createSavingsAccount(self):
        age_chk = int(input("Enter your age:"))
        if age_chk < 14 :
            print("User too young for selected account type!")
            user()
        else: 
            self.acc_no = acc_no_gen()
            self.name = input("Enter the account holder name:")
            self.balance = int(input("Enter The Initial deposit:"))
            self.acc_type = "Savings"
            
            customer_input_data = {
                self.acc_no: 
                    {
                        'Account Number': self.acc_no,
                        'Account Name': self.name.title(),
                        'Account Balance': self.balance,
                        'Account Type': self.acc_type
                    },
            }
            print(f"An account with account number {self.acc_no} has been opened for {self.name}")
            if os.stat('customer.txt').st_size == 0:
                with open('customer.txt', 'w') as obj:
                    json.dump(customer_input_data, obj, indent = 2)
            else:
                with open('customer.txt', "r+") as obj:
                        data = json.load(obj)
                        data.update(customer_input_data)
                        obj.seek(0)
                        json.dump(data, obj, indent = 2)
                        


class CheckingAccount(Account):
    def __init__(self, acc_no, name, balance, acc_type, transactions=None):
        super().__init__(acc_no, name, balance, acc_type, transactions=transactions)

    def createCheckingAccount(self):
        age_chk = int(input("Enter your age:"))
        if age_chk < 18 :
            print("User too young for selected account type!")
            user()
        else:
            self.acc_no = acc_no_gen()
            self.name = input("Enter the account holder name: ")
            self.balance = int(input("Enter The Initial deposit:"))
            self.acc_type = "Checking"

            customer_input_data = {
                self.acc_no: 
                        {
                            'Account Number': self.acc_no,
                            'Account Name': self.name.title(),
                            'Account Balance': self.balance,
                            'Account Type': self.acc_type
                        },
            }
            
            print(f"An account with account number {self.acc_no} has been opened for {self.name}")
            if os.stat('customer.txt').st_size == 0:
                with open('customer.txt', 'w') as obj:
                    json.dump(customer_input_data, obj, indent = 2)
            else:
                with open('customer.txt', "r+") as obj:
                        data = json.load(obj)
                        data.update(customer_input_data)
                        obj.seek(0)
                        json.dump(data, obj, indent = 2)


welcome()



# with open("user.txt") as jFile:
#     jObject = json.load(jFile)
#     jFile.close()


# with open("customer.txt") as jFile:
#     jObject = json.load(jFile)
#     jFile.close()

# var = input("Acc No")

# testUser = jObject[var]['Account Name']


# print(testUser)

# sean = jObject["2"]
# print(sean)




# acc = Account(123,"testacc", 250, "Savings")
# print(acc)