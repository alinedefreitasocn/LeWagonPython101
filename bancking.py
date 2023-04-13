"""
A company is opening a bank, but the coder who is designing the user
class made some errors. They need you to help them.

You must include the following:
Note: These are NOT steps to code the class

A withdraw method
    Subtracts money from balance
    One parameter, money to withdraw
    Raise a ValueError if there isn't enough money to withdraw
    Return a string with name and balance(see examples)

A check method
    Adds money to balance
    Two parameters, other user and money
    Other user will always be valid
    Raise a ValueError if other user doesn't have enough money
    Raise a ValueError if checking_account isn't true for other user
    Return a string with name and balance plus other name and other
balance(see examples)

An add_cash method
    Adds money to balance
    One parameter, money to add
    Return a string with name and balance(see examples)

Additional Notes:

Checking_account should be stored as a boolean
No input numbers will be negative
Output must end with a period
Float numbers will not be used so, balance should be integer
No currency will be used
"""
class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    #Happy coding

    def withdraw(self, withdraw_value):
        if self.balance - withdraw_value < 0:
            raise ValueError()
        else:
            self.balance = self.balance - withdraw_value
            return f"{self.name} has {self.balance}."

    def check(self, other_user, money_to_add):
        if other_user.balance - money_to_add < 0:
            raise ValueError()
        if other_user.checking_account == False:
            return ValueError()

        self.balance += money_to_add
        other_user.balance -= money_to_add
        return f"{self.name} has {self.balance} and {other_user.name} has {other_user.balance}."

    def add_cash(self, money):
        self.balance += money
        return f'{self.name} has {self.balance}.'
