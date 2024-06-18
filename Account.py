
class Account:

    def __init__(self,balance):
        self.balance=balance

    def withdraw(self,amount):
        self.balance=self.balance-amount

    def deposit(self,amount):
        self.balance=self.balance+amount

    def display(self):
        print(f'balance = {self.balance}')

acct = Account(3000)
acct.display()
acct.deposit(200)
acct.display()
acct.withdraw(700)
acct.display()
