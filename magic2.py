#Today we learn about magic and dunder methods#
class Employee:
    def __init__(self, name):
        self.name=name
    def __len__(self):#we are using length dunder __len__ method which is used to define length of object#
        i=0
        for c in self.name:
            i=i+1
        return i
    # def __init__(self, name):
    #     self.name=name
    #     print(f"{self.name}")
        
        
# obj=Employee('maaz')
# obj=Employee()
# print(obj.name)
# # Employee('maaz')#
# print(len(obj))

    # def __str__(self):#it is used to return string rep of object#
    #     return f"the name of the Employee is {self.name}"
    
    def __repr__(self):#it also returns string rep of object but it is used to recreate object#
        return f"Employee('{self.name}')"
    def __call__(self):#it is used to call objects it is an objecr call#
        print("hey i'm not good")


# obj = Employee('Maaz')
# print(obj)  # This will print: The name of the Employee is Maaz
# print(len(obj))  # This will print the length of the name, i.e., 4
