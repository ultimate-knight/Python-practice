#Today we learn about single inheritance#
class Animal:
    def __init__(self, animal, species):
        self.animal=animal
        self.species=species
        
    def make_sound(self):
        print('sound made by the animal')
        

class Dog:
    def __init__(self, animal, breed):
        Animal.__init__(self, animal, species='dog')#here dog class inheriting the properties of animal class this is called single inheritance#
        self.breed=breed
        
    def make_sound(self):
        print('bark')
        
        
d=Dog('Dog', 'Doggerman')
d.make_sound()

a=Animal('Dog', 'Dog')
a.make_sound()