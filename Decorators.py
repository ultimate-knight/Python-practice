#Today we learn about about decorator functions#
def greet(fx):#We use greet function to modify original function and return the new function
    def mfx(*args, **kwargs):
        print('good morning')
        fx(*args, **kwargs)
        print('how are u doing')
    return mfx


@greet
def hello():
    print('my name is maaz')

@greet
def add(x, y):
    print(int(x)+int(y))
    
hello()
add(12, 98)