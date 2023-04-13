# self is an important concept to understand when working with classes.
# By using the self keyword we can access the attributes and methods of the
# class in python. It helps us to represent the instance of the class that
# is passing through our methods.
# for chaning methods as in line xx we need to return self on every method
class Cat:
    def __init__(self):
        self.age = 1
        self.color = 'brown'
        self.weight = 5

    def age_10_years(self):
        self.age = 10
        return self


    def gain_weight(self):
        self.weight = 20
        return self

    def turn_grey(self):
        self.color = 'grey'
        return self

# Do not modify the code below:
cat = Cat()
print(f"My {cat.age} year old cat weighs {cat.weight} pounds and is {cat.color}.  Come back in a few years and see how he is doing.")


cat.age_10_years().gain_weight().turn_grey()
print("--------------------10 years later----------------------")
print(f"My {cat.age} year old cat now weighs {cat.weight} pounds and is {cat.color}")
