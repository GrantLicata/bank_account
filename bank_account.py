class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        if self.balance == False:
            self.balance = 0
        BankAccount.accounts.append(self)
        
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance *= (1 + self.int_rate)
        return self

    @classmethod
    def bank_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

# Validation
account1 = BankAccount(0.25, 120000)
account2 = BankAccount(0.34, 278000)
BankAccount.bank_accounts()

account1.deposit(400).deposit(300).deposit(200).withdraw(20000).yield_interest().display_account_info()
account2.deposit(300).deposit(300000).withdraw(30).withdraw(23054).withdraw(5).withdraw(93).yield_interest().display_account_info()