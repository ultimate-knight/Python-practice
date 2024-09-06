#here we learn about raising custom errors#
a=int(input('enter a number'))
if(a<5 or a>9):
    raise valueError("it isn't printable")
else:
    print(a)