#here we learn about exception handling#
num=(input('enter a number'))
print('Multiplication program')
try:
    for i in range(1, 11):
        print(f"{int(num)}X{i}={int(num)*i}")#we used try because when an error occur inside of it.It won't crash and  submit the process to the except.The except prints the program as usual and if error occcurs it warns the user of error at specific line without stopping or crashing the whole program for one specific error#
        
    b=int(input('enter a number'));
    d=[34,56]
    print(d[b]);

except:#here except is used here because if error occurs in try it will execute as usual sending the error process to except block and it will print the error#
    print('error occured')
    
# except ValueError:#it is used for values error#
    print("hey it's me error")
    
except IndexError:#it is used for index error#
    print('index error')
print("i know u don't")
        