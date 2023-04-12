"""
Create a poor_calories_counter function which takes three string arguments
and returns the total number of calories for the three items of your order.
"""
def poor_calories_counter(opt1, opt2, opt3):
    total_calories = 0
    menu = {'Hamburger' : 250,
               'Cheese Burger' : 300,
               'Big Mac' : 540,
               'McChicken' : 350,
               'French Fries' : 230,
               'Salad' : 15,
               'Coca Cola' : 150,
               'Sprite' : 150}

    MyChoise = {opt1 : menu.get(opt1, 'not found'),
                opt2 : menu.get(opt2, 'not found'),
                opt3 : menu.get(opt3, 'not found')}

    for key, value in MyChoise.items():
        if value == 'not found':
            total_calories = f'{key} {value}'
            break
        else:
            total_calories += value
    return total_calories


# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os
print("Testing with Hamburger, Cheese Burger, Big Mac")
if poor_calories_counter("Hamburger", "Cheese Burger", "Big Mac") == 1090:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with Big Mac, Salad, Coca Cola")
if poor_calories_counter("Big Mac", "Salad", "Coca Cola") == 705:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with McChicken, French Fries, Sprite")
if poor_calories_counter("McChicken", "French Fries", "Sprite") == 730:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with Shrimp, French Fries, Salad")
if poor_calories_counter("Shrimp", "French Fries", "Salad") == 'Shrimp not found':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
