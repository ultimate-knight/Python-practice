Today we learn about class methods as alternative constructors#
class Employee:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    @classmethod
    def initialize(cls, string):
        return cls(string.split('-')[0], string.split('-')[1])#we use class decorator @classmethod and we defined method with cls as class name then we are using that class to split string indices#

string="harry-120" 
emp2=Employee('maaz', 22)
emp2=Employee.initialize(string)
print(emp2.name)
print(emp2.age)
emp2=Employee(string.split("-")[0], string.split("-")[1])
print(emp2.name)
print(emp2.age) 
emp=Employee('maaz', 23)
print(emp.name)
print(emp.age)

This Python class defines a person with attributes for name and age, and includes a method to create
a new person object from a string input.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def repository(cls, string):
        name, age = string.split(",")
        return cls(name, int(age))

# Creating an instance using the repository class method
person = Person.repository("John,30")

print(person.name)  # Output: John
print(person.age)   # Output: 30
