from models.account import Account


class SavingsAccount(Account):

    INTEREST_RATE = 0.04

    def calculate_interest(self):
        return self.balance * self.INTEREST_RATE

    def get_account_type(self):
        return "Savings Account"