from models.account import Account


class CurrentAccount(Account):

    OVERDRAFT_LIMIT = 5000

    def calculate_interest(self):
        return 0

    def get_account_type(self):
        return "Current Account"