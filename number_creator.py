"""
Crazy way to create a phone number from a list of integers
using a class to define number
Training on class on Python 101 week by Le Wagon
"""
class Phone:
    def __init__(self, n):
        self.lista = n

    def code(self):
        return ''.join(str(x) for x in self.lista[:3])
    def area(self):
        return ''.join(str(x) for x in self.lista[3:6])
    def zone(self):
        return ''.join(str(x) for x in self.lista[6:])

def create_phone_number(n):
    phone = Phone(n)
    return f'({phone.code()}) {phone.area()}-{phone.zone()}'

"""
An easier way to do it would be:
def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
"""
