#here we are gonna learn about acccess modifiers#
class Employee:
    
#     pass#here this is a public class here we can access members from anywhere in a code block

a=Employee()
a.emp1=5#
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
ambient=Employee('maaz', 23);
print(ambient.name);
print(ambient.age);





        def __init__(self):
            self.__name='Harry'#This is private class here members methods and functions are not accessible in code block it is only accessible by class itself.It is denoted by double underscore __#
        
a=Employee()
    # print(a.__name);
print(a._Employee__name)#we use object instance followed by object itself using _ and it's property using __double underscore#
print(a.__dir__())#





    def __init__(self):
        self._name='maaz'
        
    def _verify(self):
        return 'code with maaz'#here it is a protected class where data members methods and variables can be accessed by class and sub classes.In order to access it we need to denote it using _underscore before methods#
    
    
class student(Employee):
    pass

stu=Employee()
stu2=student()

print(stu._name)
print(stu._verify())
print(stu2._name)
print(stu2._verify())

    
    