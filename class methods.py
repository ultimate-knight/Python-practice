#Here we learn about class methods#
class Employee:
    company='microsoft'
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")
        
    @classmethod#if we put this decorator it will change the variable for class instead of instance.If we remove it then it will become variable for instance#
    def changecompany(cls, newcompany):
        cls.company=newcompany
        
obj=Employee()
obj.name='maaz'
# obj.company='tesla'
obj.show()
Employee.changecompany('google')
obj.show()