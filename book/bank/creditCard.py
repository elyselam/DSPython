class CreditCard:

    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._account
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance

    def charge(self, price):
        '''charge card if sufficient credit limit
        return True if charge get processed'''
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount

cc = CreditCard("butt", "buttBank" , '5391 0375 9387 5309' , 1000)

print(cc.get_account())


class PredatoryCc(CreditCard):
    OVERLIMIT_FEE = 5

    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        '''True if charge goes through
        False and $5 fee if charge is denied'''
        success = super().charge(price)
        if not success:
            self._balance += PredatoryCc.OVERLIMIT_FEE
        return success


    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor
