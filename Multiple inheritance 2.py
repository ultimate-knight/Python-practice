#here we learn about the continuation of multilevel inheritance#
class Animal:
    def __init__(self, name, species):
        self.name=name
        self.species=species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"species: {self.species}")
        
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="doggerman")
        self.breed=breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"breed: {self.breed}")
            
class Doginterval(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed='rottweiler')
        self.color=color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"color: {self.color}")
        
        
o=Doginterval('doberman', 'yellow')
o.show_details()
print(Doginterval.mro())