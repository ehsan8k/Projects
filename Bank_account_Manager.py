import random
import string

class Bankaccount:
    def __init__(self, email, password, initial_balance=0):
        if '@' in email and '.com' in email:
            self.email = email
        else:
            raise ValueError('Invalid email address')
        
        if len(password) == 12:
            self.password = password
        else:
            raise ValueError('Password must be 12 characters long')
        
        self.check_balance = initial_balance
    
    def deposit(self, amount):
        self.check_balance += amount
        return f'{self.email} deposited {amount} bkr.'
    
    def withdraw(self, amount):
        if amount <= self.check_balance:
            self.check_balance -= amount
            return f'{amount} withdrawn from {self.email}.'
        else:
            return 'Insufficient balance.'
    
    def get_balance(self):
        return f'Current balance for {self.email}: {self.check_balance} bkr.'

# Example usage:
try:
    user_email = input('Please enter your email address: ')
    user_password = input('Enter your 12-character password: ')
    
    bank = Bankaccount(user_email, user_password)
    
    print(bank.get_balance())
    
    while True:
        action = input('Do you want to deposit, withdraw, or check balance? ')
        
        if action.lower() == 'deposit':
            amount = float(input('Enter deposit amount: '))
            print(bank.deposit(amount))
        elif action.lower() == 'withdraw':
            amount = float(input('Enter withdrawal amount: '))
            print(bank.withdraw(amount))
        elif action.lower() == 'check balance':
            print(bank.get_balance())
        else:
            break  # Exit loop on any other input
except ValueError as e:
    print(f'Error: {e}')
