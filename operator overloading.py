#here we learn about operator overloading#
class Vector:
    def __init__(self, i, j, k):
        self.i=i
        self.j=j
        self.k=k
    
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    
    def __add__(self, x):
        return f"{self.i+x.i}i+{self.j+x.j}j+{self.k+x.k}k"
        
   
obj=Vector(23, 45, 67)
print(obj)

obj2=Vector(34, 56, 78)
print(obj2)

print(obj+obj2)#here we used operator overloading using __add__ dundle method#



