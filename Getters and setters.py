class MyClass:
    def __init__(self, value):
        self._value = value
        
    def show(self):
        print(f"value is {self._value}")
        
    @property
    def ten_values(self):
        return 10 * self._value
    
    @ten_values.setter
    def ten_values(self, new_value):
        self._value = new_value / 10

# Object creation and method calls should be outside the class definition
obj = MyClass(10)
obj.ten_values = 67
print(obj.ten_values)
obj.show()
