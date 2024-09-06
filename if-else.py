#Today we are gonna do problems on if else in python.A statement comes under if else if the statement has indentaion#
# str1=int(input('enter a number'));
# if(str1%2==0):
#     print('even number')
# elif(str1%2!=0):
#     print('odd number')
# else:
#     print('special number')



num=int(input('enter any number'));
if(num<0):
    print('negative number')
elif(num>0):
    if(num<10):
        print('number is between 0-10')
    elif(num>10 and num<20):
        print('number is between 11-20')
    else:
        print('number is greater than 20');
else:
    print('no number');