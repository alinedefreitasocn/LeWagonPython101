"""
Let’s create an OrangeTree class which models the life of an
orange tree (its birth, life cycle and death). Our class should
incluce the following attributes: age, height, fruits, all integers,
and dead a boolean.

To simulate time passing, you will need to implement the following
instance method:

one_year_passes
pick_a_fruit

Specs
Each year, the tree should age by 1 year (it becomes older and taller,
and eventually dies).
A tree grows 1 meter per year up to and including the 10th year. Then it
stops growing
The orange tree cannot die until it reaches 50 years old.
After 50 years, the probability of dying increases each year Pyhon’s random
library might come in handy 😉.
No tree can live more than 100 years.
A tree will produce 100 fruits a year once it is more than 5 years old.
A tree will produce 200 fruits a year when it reaches 10 years old.
A tree will not produce fruits once it reaches 15 years old.
You should be able to pick a single fruit from the tree by calling the
pick_a_fruit method on your tree (but only if there are some left).
At the end of each year, the fruits which have not been picked will fall off.
"""
import random

class OrangeTree:
    def __init__(self, age=0, height=0, fruits=0, dead=False):
        self.age = age
        self.height = height
        self.fruits = fruits
        self.dead = dead

    def one_year_passes(self):
        # checking the age
        self.age += 1

        if self.age > 50:
            chances = random.randint(0, 100)
            if chances < self.age:
                self.dead = True

        # if it passes the dead test,
        # have a new year
        if self.dead == False:

            # fruits and growing
            if self.age <= 5:
                self.height = self.age
                self.fruits = 0
            elif self.age > 5 and self.age < 10:
                self.fruits = 100
                self.height = self.age
            elif self.age == 10:
                self.fruits = 200
                self.height = self.age
            elif self.age > 10 and self.age < 15:
                self.fruits = 200
                self.height = 10
            elif self.age >= 15:
                self.fruits = 0
                self.height = 10



    def pick_a_fruit(self):
        if self.fruits > 0:
            self.fruits -= 1

  # This part is not working but I would like to make it work when I have time
    # https://pynative.com/python-weighted-random-choices-with-probability/

    # def is_dead(self):
    #     if self.age > 100:
    #         age = 100
    #     else:
    #         age = self.age
    #     self.dead = random.choices([True, False],
    #                                cum_weights = (age, (100 - age)),
    #                                k=1)
