#here we learn about constructors#
class maaz:
    def __init__(self,name,age):#this is a constructor which is automatically called when object is created it an instance of class.here name and age are parameters
        self.name=name#it is the constructor's attributes which are assigned to property#
        self.age=age
        print('hey man')
    
    def method23(self):
        print(f"{self.name} is {self.age} years old")
        
a=maaz('adnan', 22)#The constrcutor is invoked whenever we create an instance of object in a program thus it prints 'hey man'#
b=maaz('ali', 23)
a.method23()#here we call method from object#
b.method23()