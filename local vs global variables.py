#here we learn about local and global variables#
x=9#here we declared a global variable it can be accessed from anywhere in a program#
print(x)

def func23():
    global x
    x=7#here we declared local variable it can be accessed inside the method#
    print("yes i'm here")


print(x)#here it will print global variable it is outside the scope of func23 method# 
func23()
print(x)#here it will print local variable because it is declared below the method#