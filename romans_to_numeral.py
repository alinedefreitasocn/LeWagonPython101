"""
Let’s use dictionarys to help us quickly convert Roman Numerals to integers.
Write a function roman_to_int It should take one argument, a string, and
convert it into its corresponding integer eg:

roman_to_int(‘IV’) #=> 4
roman_to_int(‘XVI’) #=> 16
roman_to_int(‘MI’) #=> 1001

Hint - you might consider including 4/40/400 and 9/90/900 in your dictionary
"""

def roman_to_int(st):
    numeral = 0
    romans = {'I' : 1,
              'IV' : 4,
              'V' : 5,
              'IX' : 9,
              'X' : 10,
              'XL' : 40,
              'L' : 50,
              'XC' : 90,
              'C' : 100,
              'CD' : 400,
              'D' : 500,
              'CM' : 900,
              'M' : 1000}

    while len(st) > 2:
        if romans.get(st[-2:], False):
            numeral += romans.get(st[-2:])
            st = st[:-2]
        else:
            numeral += romans.get(st[-1])
            st = st[:-1]

    while len(st) > 0:
        if romans.get(st, False):
            numeral += romans.get(st)
            break
        else:
            numeral += romans.get(st[-1])
            st = st[:-1]

    return numeral
