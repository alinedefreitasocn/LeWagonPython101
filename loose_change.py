"""
you must create a function that takes an amount of US currency in cents,
and returns a dictionary/hash which shows the least amount of coins used
to make up that amount. The only coin denominations considered in this
exercise are: Pennies (1¢), Nickels (5¢), Dimes (10¢) and Quarters (25¢).
Therefor the dictionary returned should contain exactly 4 key/value pairs.

Training the use of classes from the python 101 week by Le Wagon
"""
class Coins:
    def __init__(self, amount):
        self.amount = amount

    def do_you_have(self, coin):
        n_coins = self.amount // coin
        if n_coins > 0:
            self.amount = self.amount - (n_coins * coin)
            return n_coins
        else:
            return 0


def loose_change(cents):
    money = Coins(cents)
    change_dict = {'Quarters': money.do_you_have(25),
                   'Dimes': money.do_you_have(10),
                   'Nickels': money.do_you_have(5),
                  'Pennies': money.do_you_have(1)
                  }
    return change_dict
