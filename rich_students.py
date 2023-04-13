"""
Suppose you have students (defined by the class Student) who each have an
amount of money (in bills of five, ten and twenty euro). We want to be
able to compare them based on their wealth. Let’s create a class Student
which will store all their information and help with comparing

Specs
When initializing a Student, you should require 4 additional arguments,
the student’s name and the number of bills they own (fives, tens and twenties)
Implement a wealth method on Student. When called it should return the
total wealth of the student
Implement a compare method which takes one argument, another student, and
returns the name of the richer student
Optional
Implement an advanced_compare method which takes one argument, a list of
students. When called, it should return a list of all the student’s names
sorted from most wealthy to least wealthy….don’t forget to include the
student instance the method was called on in the sort
"""
class Student():
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self. twenties = twenties

    def wealth(self):
        return  ((self.fives * 5) +
                        (self.tens * 10) +
                        (self.twenties * 20))

    def compare(self, another_std):
        if self.wealth() > another_std.wealth():
            return f'{self.name}'
        else:
            return f'{another_std.name}'

    def advanced_compare(self, lista):
        students = []
        students.append([self.name, self.wealth()])
        for student in lista:
            students.append([student.name, student.wealth()])
        sorted_students = sorted(students, key=lambda x: x[1], reverse = True)
        names_sorted = [name[0] for name in sorted_students]
        return names_sorted
