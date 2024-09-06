# #here we learn about finally keyword#
try:
    num=int(input('enter a number'))
    a=[12,34,56,67,78]
    print('a[num]')
except:
    print('error occured')
finally:#finally block executes no matter what even if there's an error or not#
    print('it will always be printed');



def func1():
    try:#This block execute when the answer is right that's why it is denoted as return 1#
        num=int(input('enter a number'));
        a=[34,45,67,78]
        print(a[num])
        return 1
    except:#This block execute when the answer is wrong that's why it is denoted as return 0#
        print("hey it's an error")
        return 0
    finally:#This block executes no matter what#
        print("it's me")
        return 2
x=func1()
print(x);