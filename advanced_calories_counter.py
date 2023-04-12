"""
Now, let’s say you want to improve your calorie counter,
so that it can accept a list of drinks, burgers, sides,
and MEALS.

You may want to store these meals in another constant.
Note: don’t try to pre-compute the calories for each meal,
just store the dishes that make up the meal. How do you
think you could represent the dishes in each meal?

Let’s now create an advanced_calories_counter function
that will enable us to calculate calories of a combination
of both our meals and our individual dishes
"""

meals = {'Happy Meal' : ['Cheese Burger',
                         'French Fries',
                         'Coca Cola'],
        'Best Of Big Mac' : ['Big Mac',
                             'French Fries',
                             'Coca Cola'],
        'Best Of McChicken' : ['McChicken',
                               'Salad',
                               'Sprite']}

calories = {'Hamburger' : 250,
               'Cheese Burger' : 300,
               'Big Mac' : 540,
               'McChicken' : 350,
               'French Fries' : 230,
               'Salad' : 15,
               'Coca Cola' : 150,
               'Sprite' : 150}

def advanced_calories_counter(lista):
    total_calories = 0
    for item in lista:
        if meals.get(item, 'not found') == 'not found':
            if calories.get(item, 'not found') == 'not found':
                total_calories = f'{item} not found'
                break
            else:
                total_calories += calories.get(item)
        else:
            for i in meals.get(item):
                total_calories += calories.get(i)

    return total_calories
