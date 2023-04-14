"""
Complete the class Dessert:

create instance variables for name and calories
create an instance method healthy which returns a bool. A dessert
instance with fewer than 200 calories would be considered healthy
create an instance method delicious which returns a bool. All dessert
instances should return True

Create the class JellyBean:

JellyBean should be a child of the Dessert class
JellyBean should take three arugments - name, calories, flavor
Keep your init method DRY with super()
JellyBean’s delicious method should return the default set in the parent
class, unless its flavor is black licorice, which is not delicious

I learn that everytime you want to go back to the ihneret class you use
the super(), like in the definition of delicious on the JellyBean class.
"""
class Dessert:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories


    def healthy(self):
        return self.calories < 200

    def delicious(self):
        return True

class JellyBean(Dessert):
    def __init__(self, name, calories, flavor):
        super().__init__(name, calories)
        self.flavor = flavor

    def delicious(self):
        if self.flavor == 'black licorice':
            return False
        else:
            return super().delicious()
