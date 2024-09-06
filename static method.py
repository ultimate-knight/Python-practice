#here we are gonna learn about static method#
class practice:
    def __init__(self, name):
        self.name=name
        
    def method(self):
        print('hey man')
        
    def process(self):
        print('how u doing')
        
        
    @staticmethod#here we use these decorator because it won't require us to add
    def add(a,b):
        return a+b
    

obj=practice('maaz')
# print(obj.name)
# print(obj.method())
# print(obj.process())
obj.add(13,34)
# print(obj.add(12,23))
print(practice.add(23,67))
