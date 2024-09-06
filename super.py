#Today we learn about super keyword#
class employee:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
class programmer(employee):#child class programmer inherits from parent class employee#
    def __init__(self,name,age,lang):
        # self.name=name#instead of doing this#
        # self.age=age
        #do this#
        super().__init__(name, age)
        self.lang=lang
        
obj=employee('maaz', 22)
obj2=programmer('saif', 24, 'english')
print(obj.name)
print(obj2.name)
print(obj.age)
print(obj2.lang)