#here we learn about instance and class variable#
class painstake:
    employee='anil'
    currency=0
    def __init__(self,name):
        self.name=name
        self.value=9
        painstake.currency+=1
        
    
    def method(self):
        print(f"{self.name} is a software engineer for {self.value} years and {self.employee} is a manager and there {self.currency} employees")
        
        
   



a=painstake('maaz')
a.value=5#the value is changed for maaz and printed the same#
a.employee='mazhar'
a.method()
b=painstake('adnan')
b.method()