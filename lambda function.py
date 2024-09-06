#here we learn about lambda functions#
# def cube(x):
#     return x+5
# def rouble(x, value):
#     return 8+x(value)
# def rouble(x, value):
#     return 6+x(value)
cube=lambda x: x+9#we use lambda which is an anonymous function which is used whem used to execute short one line code whereby we use variable=lambda var(arg): return statement#
square=lambda y: y*91
avg=lambda x,y: (x+y)/2
cube=lambda x:x*x*x
print(square(9))
print(cube(6))
print(avg(9,308))
print(rouble(cube, 8))#here we declared function inside of function to fetch it's content and to apply on the current code#
print(rouble(lambda x:x*x*x, 2))#here we directly declared function inside print statement or u could say a recursion type#