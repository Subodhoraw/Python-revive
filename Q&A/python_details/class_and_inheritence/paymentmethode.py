class payment_method:
    def process_payment(self, amount):
        raise NotImplementedError("you must override this error")
    
class creditcardpayment(payment_method):
    def process_payment(self,amount):
        print(f" Processing Credit card payment of ${amount}")

class UPIpayment(payment_method):
    def process_payment(self, amount):
       print(f" Processing Credit card payment of ${amount}")

    
class debitcardpayment(payment_method):
    def process_payment(self, amount):
        print(f" Processing Credit card payment of ${amount}")

    
class cryptopayment(payment_method):
    def process_payment(self, amount):
        print(f" Processing Credit card payment of ${amount}")


payments = [creditcardpayment(),UPIpayment(),debitcardpayment(),
            cryptopayment()

]
for method in payments:
    method.process_payment(999)
