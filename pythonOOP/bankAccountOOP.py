class Account():
    
    def __init__(self,owner,balance):
        
        self.owner = owner
        self.balance = balance
    
    def withdraw(self,amount):
        if(amount > self.balance):
            print('Not to much balance in your account ')
        else:
            self.balance = self.balance-amount
            print(f'Amount debbited from your account is {amount}')
            print(f'Your Current Account balance is : {self.balance}')
    
    def deposit(self,amount):
        
        self.balance += amount
        print(f'Amount deposited to your account ')
        print(f'Your Current Account balance is : {self.balance}')

acc1 = Account('Hrishab',1000)
acc2 = Account('Rahul',2000)


acc1.deposit(2000)
acc1.withdraw(500)   

acc2.deposit(300)
acc2.withdraw(5000)