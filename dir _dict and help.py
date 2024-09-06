# #here we learn about dir _dict and help methods#
x=[1,2,3]
print(dir(x))#dir method returns all the methods and attributes associated with object#
print(x.__doc__)


class employee:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
x=employee('baqtiyaar', 22)
print(x.__dict__)#here it returns object elements in dictionary format#
print(help(employee))#here it will provide the description of the object contents#