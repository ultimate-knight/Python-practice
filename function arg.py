#Here we learn about function arguments#
def arg(a=9, b=8):
    print(a);
    print(b);
arg(23, 87);#Here as u can see it is considered values for function calls ignoring paramter values#


def arg(a=10, b=15):
    print(a+b);
arg(19)#here it will replace 10 with 19 and b value remain unchanged if we provide only one argument in function call then first value will be printed#



def arg1(a, b, c=23):
    print((a+b+c)/2); # arg1(12,24);#here these are the values of a and b#HB,A


def average(*variables):#this became list when i placed * before the argument#
    print(type(variables));
    sum=0;
    for i in variables:
        sum=sum+i
    print('Average is:', (sum/len(variables)));
average(12,34,45,67)



def arg2(**variables):
    print("hello", variables['fname'], variables['lname'], variables['gname']);#here we declared dictionary by two pointers** in parameter these are variables['fanames'] are properties of variable object#

arg2(fname='md', lname='baqtiyaar', gname='ali');



# def average(*variables):#this became list when i placed * before the argument#
#     print(type(variables));
#     sum=0;
#     for i in variables:
#         sum=sum+i
#     return sum/len(variables)#here as u can see when i used return function it stores the whole expression sum/avg in avrage function because they are the property of average function#
# c=average(12,34,45,67);
# print(c);

    