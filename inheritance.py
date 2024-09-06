#we are learning here about inheritance#
class Employee:
    def __init__(self, name, id):
        self.name=name;
        self.id=id;
        
    def method34(self):
        print(f"{self.name} have a {self.id} as roll number")
        

class employer(Employee):
    def method45(self):
        print('everything is good');

f=Employee('baqtiyaar', 160319733025);
f.method34();
g=employer('adnan', 160319733027);
g.method45();
