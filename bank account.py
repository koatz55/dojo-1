

int_rate = 0.01

class BankAccount:
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self,int_rate,balance): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # don't worry about user info here; we'll involve the User class soon
    @classmethod
    def all_info(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
            print("account balance: ",account.balance)
            print("account interest rate:",account.int_rate)
        print("Total balance: ",sum)
        return sum
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        if self.balance < amount:
            print("insufficient balance: charging a $5 fee...")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        # your code here
        print("balance:", self.balance)
        return self
    def yield_interest(self):
        # your code here
        self.balance =  self.balance + (self.balance * self.int_rate)
        return self

Moise_bank_account = BankAccount(0.01,0)
ronny_bank_account = BankAccount(0.01,0)

Moise_bank_account.deposit(500).deposit(300).deposit(2000).withdraw(1300).yield_interest().display_account_info()
ronny_bank_account.deposit(500).deposit(3000).withdraw(300).withdraw(300).withdraw(400).withdraw(2600.).yield_interest().display_account_info()
BankAccount.all_info()

class User:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        self.savings_accounts = []
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def make_interest(self):
        self.account.yield_interest()
        return self

    def show_balance(self):
        name = self.name 
        print(name , end=" "),self.account.display_account_info()
        return self
        
    def create_savings_account(self, int_rate, balance):
        self.savings_accounts.append(BankAccount(int_rate, balance))
        return self
    def pick_savings_accounts(self):
        for i in range(len(self.savings_accounts)):
            print("Savings Account number:",i,"balance:",self.savings_accounts[i].balance)
            print("Savings Account number:",i,"interest rate:",self.savings_accounts[i].int_rate)
        num = self.get_num()
        num = int(num)
        print("Savings Account number:",num,"balance:",self.savings_accounts[num].balance)
        withdraw_amount = int(input("please enter your amount to withdraw: "))
        print("Savings Amount to withdraw:", withdraw_amount)
        self.savings_accounts[num].withdraw(withdraw_amount)
        deposit_amount = int(input("please enter your deposit amount: "))
        print("Savings Amount to Deposit:", deposit_amount)
        self.savings_accounts[num].deposit(deposit_amount)
        print("Savings Account number:",num,"balance:",self.savings_accounts[num].balance)
        return self

    def get_num(self):
        num = input("please enter your savings account number you want to access:  ")
        num = int(num)
        # if int(num) < 0 or int(num) >= len(self.savings_accounts):
        #     print("Please enter a  valid savings account number you want to access!")
        #     self.get_num() # dose not work yet 
        return num

    def transfer_money(self, amount, other_user):        
        self.make_withdraw(amount)
        other_user.make_deposit(amount)


Johnny = User("Johnny","coolguy82@pmail.com")
gumball = User("gumball","bluecat@pmail.com")

Johnny.show_balance().make_deposit(500).make_withdraw(200).show_balance()
Johnny.create_savings_account(0.5,200)
Johnny.create_savings_account(0.7,600)
print(Johnny.savings_accounts[0].balance)
Johnny.pick_savings_accounts()
gumball.create_savings_account(0.5,100)
gumball.pick_savings_accounts()
Johnny.transfer_money(100,gumball)
gumball.show_balance()
Johnny.show_balance()
