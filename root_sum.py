"""
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more
than one digit, continue reducing in this way until a single-digit
number is produced. The input will be a non-negative integer.
"""
def not_single_digit(dig):
    total = 0
    while dig >= 10:
        print(f'{dig} more than one digit')
        print(f'adding {dig % 10} to total')
        total += dig % 10
        print(f'Now total is {total}')
        dig = dig // 10
        print(f'and the new number is {dig}')
    total += dig

    return total

def digital_root(n):
    while n >= 10:
        print('Starting a while in the main function')
        n = not_single_digit(n)

    return n
