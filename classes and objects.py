#here we learn about classes and objects#
class objects:
    name='maaz'#these are the properties of object class as u studied in javascript#
    age=22
    occupation="software engineer"
    def method(self):#method which is a function called inside a class#
        # print(f"{objects.name} is a {objects.occupation}")
        print(f"{self.name} is a {self.occupation}")
        

a=objects()#assigning objects to variables#
b=objects()
b.name='amaan'#the objects properties become variable properties#
age=22
a.name='adnan'
a.age=27
a.method()#using method function on variables
b.method()
objects.method()#here it won't work because u can't call method on class itself#
a=objects()#u have to call a method on instance of class which is a here and class is objects#
a.method()
a.name='baqtiyaar'
a.age=23
a.occupation='hr'
a.method()