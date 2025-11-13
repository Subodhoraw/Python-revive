class Bankaccount:
    def __init__(self, account_number,balance):
        self.account_number = account_number
        self.balance = balance
    def __str__(self):
        return f"Account ending in {self.account_number[-4:]}: ${self.balance:,.2f}"
    def __repr__(self):
        return f"BankAccount(account_number='{self.account_number}',balance ={self.balance})"
account = Bankaccount("123456789",5420.200)
print("Your account:",str(account))  
print("Debug:", repr(account))