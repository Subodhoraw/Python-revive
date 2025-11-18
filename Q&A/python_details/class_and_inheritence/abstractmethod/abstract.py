from abc import ABC, abstractmethod
class paymentGateway(ABC):
    @abstractmethod
    def process(self,amount):
        pass
class creditcardpayment(paymentGateway):
    def process( self,amount):
        print(f"credit card amount {amount} processing...")
        print(f" {amount} sucessfully paid")
class debitcardpayment(paymentGateway):
    def process(self,amount):
        print(f" debitcard payment amount{amount} processing")
        print(f" {amount} debit card payment done ")
class cryptopayment(paymentGateway):
    def process(self,amount):
        print(f"{amount}USDT is in processing")
        print(f"payment {amount} has benn done")

payments = [creditcardpayment(), debitcardpayment(), cryptopayment()]
for method in payments:
    method.process(500)

