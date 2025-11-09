class Bankaccount:
    bank_name = "Python Bank"
    total_accounts = 0
    intrest_rate = 0.03

    def __init__(self, owner, balance):
        #instance variables
        self.owner = owner
        self.balance = balance
        Bankaccount.total_accounts += 1
        self.account_number = f"ACC{Bankaccount.total_accounts:04d}"
    def apply_intrest(self):
        """Apply intrest using class  variable rate """
        intrest = self.balance * Bankaccount.intrest_rate
        self.balance += intrest
        return f"intrest applied : ${intrest :.2f}"
    def display_info(self):
        return (f" Bank: {Bankaccount.bank_name}\n"
                f"Account: {self.account_number}\n"
                f"Owner: {self.owner}\n"
                f"Balance: ${self.balance:.2f}\n"
                f"intrest Rate: {Bankaccount.intrest_rate * 100}%")
acc1 = Bankaccount("Alice", 1000)
acc2 = Bankaccount("Subodh",500000)
acc3 = Bankaccount("Bibek",50000)
print(acc1.display_info())
print(f"\nTotal accounts created: {Bankaccount.total_accounts}")
#change intrest rate for all account
print(f"{'change intrest rate for all account':^40}")
Bankaccount.intrest_rate = 0.05
print(acc1.display_info())
print(acc1.apply_intrest())

print(f"\n{acc1.owner}'s new balance: ${acc1.balance:.2f}")
print(f"{acc2.owner}'s Balace: ${acc2.balance:.2f}")
                
