#here we learn about multiple inheritance#
class Employee:
    def __init__(self, name):
        self.name=name
    
    def show(self):
        print('it is {self.name}')
        
class dancer:
    def __init__(self, dance):
        self.dance=dance
    
    def show(self):
        print(it is {self.dance})
        
class dancerEmployee(Employee, dancer):
    def __init__(self, dance, name ):
        self.name=name
        self.dance=dance
        
o=dancerEmployee('maaz', 'freestyle')
print(o.name)
print(o.dance)
o.show()
print(dancerEmployee.mro())