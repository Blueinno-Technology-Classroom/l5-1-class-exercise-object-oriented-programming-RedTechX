print()
##################################################
'''
Q1a: 
'''
print('x = 9, y = 2')
print()
##################################################
'''
Q1b: 
'''
print('x = 27, y = 2')
print()
##################################################
'''
Q2:
'''

class Name:
    def __init__(self, fn: str, ln: str):
        self.fn = fn
        self.ln = ln
    
    
##################################################

#Q3:

    def normal_order(self) -> str:
        return f'{self.fn} {self.ln}'
    
    
    def reverse_order(self) -> str:
        return f'{self.ln} {self.fn}'


jf = Name('Jeremy', 'FANG')

print(jf.normal_order())
print(jf.reverse_order())
print()

##################################################
'''
Q4 to Q7:
'''

class BankAccount:
    def __init__(self, name: str):
        self.name = name
        self.balance = 0.0
        self.withdrawal_fee = 2.0
        self.transfer_fee = 5.0
    
    
    def deposit(self, value: int|float):
        if value <= 0:
            raise ValueError
        
        self.balance += value
    
    
    def withdraw(self, value: int|float):
        if value <= 0:
            raise ValueError

        if self.balance < value + self.withdrawal_fee:
            raise ValueError
        
        self.balance -= value + self.withdrawal_fee
    
    
    def transfer(self, recipient, value: int|float):
        if value <= 0:
            raise ValueError
        
        if self.balance < value + self.transfer_fee:
            raise ValueError
        
        self.balance -= value + self.transfer_fee
        recipient.deposit(value)
    
    
    def print(self):
        print(f'{self.name}: {self.balance}')


jeremy = BankAccount('Jeremy')
felix = BankAccount('Felix')

jeremy.deposit(50)
jeremy.print()
felix.deposit(20)
felix.print()
jeremy.withdraw(13)
jeremy.print()
jeremy.transfer(felix, 15)
jeremy.print()
felix.print()

##################################################
