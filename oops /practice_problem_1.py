# make BankAccount class with methods to deposit, withdraw, and check balance

class BankAccount:
    def __init__(self, balance, withdraw, deposit):
        self.balance = balance
        self.deposit = deposit
        self.withdraw = withdraw
        
        
my_account = BankAccount(100,20,30)
print(my_account.deposit)
print(my_account.withdraw)
print(my_account.balance)
