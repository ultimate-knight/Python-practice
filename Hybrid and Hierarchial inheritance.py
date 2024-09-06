#here we learn about hierarchial and hybrid inheritance#

#This is Hierachial inheritance#
class Animal:
    def speak(self):
        print('my name is maaz')
        
class Dog(Animal):
    def bark(self):
        print('how dare u bark')
        
class cat(Animal):
    def meow(self):
        print('How dare u meow')
        
d=Dog()
c=cat()
d.bark()
d.speak()
c.meow()
c.speak()





#This is Hybrid inheritance#
# Base class
# class Animal:
#     def speak(self):
#         print("Animal speaks")

# # Intermediate class (single inheritance)
# class Mammal(Animal):
#     def walk(self):
#         print("Mammal walks")

# # Another base class for multiple inheritance
# class WingedAnimal:
#     def fly(self):
#         print("Winged animal flies")

# # Derived class (multiple and hierarchical inheritance)
# class Bat(Mammal, WingedAnimal):
#     def nocturnal(self):
#         print("Bat is nocturnal")

# # Creating an object of the derived class
# bat = Bat()

# # Calling methods from all inherited classes
# bat.speak()      # From Animal class
# bat.walk()       # From Mammal class
# bat.fly()        # From WingedAnimal class
# bat.nocturnal()  # From Bat class
