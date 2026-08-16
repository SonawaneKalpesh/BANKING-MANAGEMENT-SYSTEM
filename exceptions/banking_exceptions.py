class BankingError(Exception):
   
    pass


class InvalidAmountError(BankingError):
    
    pass


class InsufficientBalanceError(BankingError):
   
    pass


class AccountNotFoundError(BankingError):
   
    pass


class CustomerNotFoundError(BankingError):
   
    pass


class AccountAlreadyExistsError(BankingError):
    
    pass


class InactiveAccountError(BankingError):
   
    pass


class InvalidAccountTypeError(BankingError):
    
    pass