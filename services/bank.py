from exceptions.banking_exceptions import *
from exceptions.banking_exceptions import AccountNotFoundError, CustomerNotFoundError
from exceptions.banking_exceptions import InvalidAmountError
from models.customer import Customer


class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}
        self.transactions = {}
        self.customer_id_counter = 1

    def register_customer(self, name, email, phone, address):
        customer_id = self.customer_id_counter
        self.customers[customer_id] = Customer(customer_id, name, email, phone, address)
        self.customer_id_counter += 1
        self.pin="0000"
        return customer_id

    def create_account(self, customer_id, account_type):
        if customer_id not in self.customers:
            raise CustomerNotFoundError("Customer ID does not exist.")
        account_number = len(self.accounts) + 1
        self.accounts[account_number] = {
            "customer_id": customer_id,
            "account_type": account_type,
            "balance": 0.0
        }
        return account_number

    def check_pin(self, pin):

        if self.pin == "0000":
            print("set your pin")
            self.pin=input("enter your pin : ")
        return pin == self.pin

    

    def find_customer(self, customer_id):
        if customer_id not in self.customers:
            raise CustomerNotFoundError("Customer ID does not exist.")
        return self.customers[customer_id].get_customer_details()

    def find_account(self, account_number):
        if account_number not in self.accounts:
            raise AccountNotFoundError("Account number does not exist.")
        account = self.accounts[account_number]
        customer = self.customers[account["customer_id"]]
        return {
            "account_number": account_number,
            "customer_details": customer.get_customer_details(),
            "account_type": account["account_type"],
            "balance": account["balance"]
        }

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            raise AccountNotFoundError("Account number does not exist.")
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")
        self.accounts[account_number]["balance"] += amount
        self.transactions.setdefault(account_number, []).append({
            "type": "deposit",
            "amount": amount
        })

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            raise AccountNotFoundError("Account number does not exist.")
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if self.accounts[account_number]["balance"] < amount:
            raise ValueError("Insufficient balance.")
        self.accounts[account_number]["balance"] -= amount
        self.transactions.setdefault(account_number, []).append({
            "type": "withdrawal",
            "amount": amount
        })

    def transfer(self, from_account, to_account, amount):
        if from_account not in self.accounts or to_account not in self.accounts:
            raise AccountNotFoundError("One or both account numbers do not exist.")
        if amount <= 0:
            raise InvalidAmountError("Transfer amount must be positive.")
        if self.accounts[from_account]["balance"] < amount:
            raise InvalidAmountError("Insufficient balance in the source account.")
        self.accounts[from_account]["balance"] -= amount
        self.accounts[to_account]["balance"] += amount
        self.transactions.setdefault(from_account, []).append({
            "type": "transfer_out",
            "amount": amount,
            "to_account": to_account
        })
        self.transactions.setdefault(to_account, []).append({
            "type": "transfer_in",
            "amount": amount,
            "from_account": from_account
        })

    def check_balance(self, account_number):
        if account_number not in self.accounts:
            raise AccountNotFoundError("Account number does not exist.")
        return self.accounts[account_number]["balance"]

    def view_account_details(self, account_number):
        if account_number not in self.accounts:
            raise AccountNotFoundError("Account number does not exist.")
        account = self.accounts[account_number]
        customer = self.customers[account["customer_id"]]
        return {
            "account_number": account_number,
            "customer_details": customer.get_customer_details(),
            "account_type": account["account_type"],
            "balance": account["balance"]
        }

    def transaction_history(self, account_number):
        if account_number not in self.accounts:
            raise AccountNotFoundError("Account number does not exist.")
        return self.transactions.get(account_number, [])

