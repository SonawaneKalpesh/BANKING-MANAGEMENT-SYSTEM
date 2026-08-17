from services.bank import Bank
from exceptions.banking_exceptions import *
from models.account import Account

def register():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone: ")
    address = input("Enter customer address: ")
    customer_id = customer.register_customer(name, email, phone, address)
    print(f"Customer registered successfully. Customer ID: {customer_id}")
    print("--------------------------------")

def createAccount():
    customer_id = int(input("Enter customer ID: "))
    account_type = input("Enter account type (savings/current): ")
    account_number = customer.create_account(customer_id, account_type)
    print(f"Account created successfully. Account Number: {account_number}")
    print("--------------------------------")

def deposit():
    pin = input("Enter your PIN: ")
    if customer.check_pin(pin):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))
        customer.deposit(account_number, amount)
        print(f"Deposited {amount} to account number {account_number}.")
        print("--------------------------------")
    else:
        print("Invalid PIN. Deposit failed.")
        print("--------------------------------")

def withdraw():
    pin = input("Enter your PIN: ")
    if customer.check_pin(pin):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount: "))
        customer.withdraw(account_number, amount)
        print(f"Withdrew {amount} from account number {account_number}.")
        print("--------------------------------")
    else:
        print("Invalid PIN. Withdrawal failed.")
        print("--------------------------------")

def transfer():
    pin = input("Enter your PIN: ")
    if customer.check_pin(pin):
        from_account = int(input("Enter your account number: "))
        to_account = int(input("Enter recipient's account number: "))
        amount = float(input("Enter transfer amount: "))
        customer.transfer(from_account, to_account, amount)
        print(f"Transferred {amount} from account {from_account} to account {to_account}.")
        print("--------------------------------")
    else:
        print("Invalid PIN. Transfer failed.")
        print("--------------------------------")

def checkBalance():
    pin = input("Enter your PIN: ")
    if customer.check_pin(pin):
        account_number = int(input("Enter account number: "))
        balance = customer.check_balance(account_number)
        print(f"Account number {account_number} has a balance of {balance}.")
        print("--------------------------------")
    else:
        print("Invalid PIN. Balance check failed.")
        print("--------------------------------")

def viewAccountDetails():
    pin = input("Enter your PIN: ")
    if customer.check_pin(pin):
        account_number = int(input("Enter account number: "))
        details = customer.find_account(account_number)
        print(f"Account Details for account number {account_number}:")
        print(details)
        print("--------------------------------")
    else:
        print("Invalid PIN. Cannot view account details.")
        print("--------------------------------")

def transactionHistory():
        account_number = int(input("Enter account number: "))
        history = customer.transaction_history(account_number)
        print(f"Transaction History for account number {account_number}:")
        for transaction in history:
            print(transaction)
        print("--------------------------------")
    

def searchCustomer():
    customer_id = int(input("Enter customer ID to search: "))
    try:
        details = customer.find_customer(customer_id)
        print(f"Customer Details for customer ID {customer_id}:")
        print(details)
        print("--------------------------------")
    except ValueError as e:
        print(str(e))
        print("--------------------------------")

def closeAccount():
    pin = input("Enter your PIN: ")
    if customer.check_pin(pin):
        account_number = int(input("Enter account number to close: "))
        try:
            customer.close_account(account_number)
            print(f"Account number {account_number} closed successfully.")
            print("--------------------------------")
        except ValueError as e:
            print(str(e))
            print("--------------------------------")
    else:
        print("Invalid PIN. Cannot close account.")
        print("--------------------------------")

try:
    customer = Bank()
except Exception as e:
    print("An error occurred while initializing the banking system:", str(e))

try:
    while True:
        print(" BANKING MANAGEMENT SYSTEM")
        print("1.Register Customer")
        print("2.Create Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Check Balance")
        print("7. View Account Details6.")
        print("8. Transaction History")
        print("9. Search Customer")
        print("10. Close Account")
        print("11. Exit")
        choice=int(input("enter your choice : "))

        match(choice):
            case 1:
                print("Register Customer")
                register()

            case 2:
                print("Create Account")
                createAccount()

            case 3:
                deposit()

            case 4:
                withdraw()
            case 5:
                transfer()
            case 6:
                checkBalance()
            case 7:
                viewAccountDetails()
            case 8:
                transactionHistory()
            case 9:
                searchCustomer()
            case 10:
                closeAccount()
            case 11:
                print("Thank you for using the Banking Management System.")
                break

            case _:
                print("Invalid choice. Please try again.")

except Exception as e:
    print("An error occurred:", str(e))
