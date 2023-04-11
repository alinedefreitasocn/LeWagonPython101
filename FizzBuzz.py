""" Write a function fizz_buzz which takes a single number as an argument, 
and returns a list of numbers from 1 to that number, but replaces some of 
them according to these rules:

If the number is divisible by 3, then replace it with ‘Fizz’
If the number is divisible by 5, then replace it with ‘Buzz’
If the number is divisible by both 3 and 5, then replace it with ‘FizzBuzz’
e.g.

fizz_buzz(7)
# => [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', """

def fizz_buzz(number):
    final_list = []
    for n in range(1, number + 1):
        if (n % 3 == 0) and (n % 5 == 0):
            final_list.append('FizzBuzz')
        elif n % 3 == 0:
            final_list.append('Fizz')
        elif n % 5 == 0:
            final_list.append('Buzz')
        else:
            final_list.append(n)
    return final_list

  


# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os
print("Testing your Answer:")
if len(fizz_buzz(5)) == 5:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your Fizz:")
if fizz_buzz(20).count('Fizz') == 5:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your Buzz:")
if fizz_buzz(33).count('Buzz') == 4:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your FizzBuzz:")
if fizz_buzz(50).count('FizzBuzz') == 3:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
