"""
This is your first potion class in Hogwarts and professor
gave you a homework to figure out what color potion will
turn into if he'll mix it with some other potion. All potions
have some color that written down as RGB color from [0, 0, 0]
to [255, 255, 255]. To make task more complicated teacher will
do few mixing and after will ask you for final color. Besides
color you also need to figure out what volume will have potion
after final mix.

Based on your programming background you managed to figure that
after mixing two potions colors will mix as if mix two RGB colors.
For example, if you'll mix potion that have color [255, 255, 0]
and volume 10 with one that have color [0, 254, 0] and volume 5,
you'll get new potion with color [170, 255, 0] and volume 15. So
you decided to create a class Potion that will have two properties:
color (a list (a tuple in Python) with 3 integers) and volume (a number),
and one method mix that will accept another Potion and return a mixed Potion.
"""

import math

class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume

    def mix(self, other):

        selfmix = [color * self.volume for color in self.color]
        othermix = [c * other.volume for c in other.color]

        new_color = tuple([math.ceil((selfmix[i] + othermix[i])/(self.volume + other.volume))
                     for i in range(len(self.color))])

        new_volume = self.volume + other.volume
        return Potion(new_color, new_volume)
