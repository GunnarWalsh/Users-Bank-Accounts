class BankAccount:
    startingBalance = 0 # <-- figure out to incorperate @classmethood
    def __init__(self, int_rate, balance): 
        self.intrest = int_rate
        self.bal = balance
        self.users = []
    def deposit(self, amount):
        if amount > 0:
            self.bal += amount
            # BankAccount.startingBalance == self.bal <-- figure out to incorperate @classmethood
            print("+ Balance:" , self.bal)
            return self
    def withdraw(self, amount):
        if self.bal > 0:
            self.bal -= amount
            print("- Balance:" , self.bal)
            # BankAccount.startingBalance == self.bal  <-- figure out to incorperate @classmethood
            return self
        else:
            self.bal -= 5
            print("Insufficient Funds: Charging a $5 fee")
            # print(BankAccount.startingBalance)  <-- figure out to incorperate @classmethood
            return self
    def display_account_info(self):
            # BankAccount.startingBalance += self.bal  <-- figure out to incorperate @classmethood
            print("Account Balance:" , self.bal)
            return self
    def yield_interest(self):
        if self.bal > 0:
            self.bal += self.bal * self.intrest
            print("Intrest:" , self.bal)
            return self
        else:
            return self
    def add_new_account(self, new_user):
        self.users.append(new_user)
    
    
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        self.user_acount = None
    
    def make_deposit(self):
        self.account.deposit(100)
        print("Deposit Succesful")
    def make_withdraw(self):
        self.account.withdraw(100)
        print("withdraw Succesful")
    def display_user_balance(self):
        self.account.display_account_info
    def __repr__(self):
        return f'BankAccount("{self.account}")'






account_1 = BankAccount(0.01, 0)
account_2 = BankAccount(0.01, 0)
user_1 = User("gunnar" , "gunnarwalsh@gmail.com")
user_2 = User("matison" , "mcain@gmail.com")

user_1.user_acount = account_1
user_2.user_acount = account_2
account_1.add_new_account(user_1)

account_1.deposit(300).display_account_info()
account_2.deposit(50).display_account_info()

print(account_1.users[0].name)





# .deposit(100).deposit(50).withdraw(400).yield_interest() 
# .deposit(20).withdraw(100).withdraw(10).withdraw(12.82).withdraw(16.47).yield_interest()