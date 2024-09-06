#here we are learning about functions#
def gmean(a,b):
    mean=(a*b)/(a+b);
    print(mean);
    
def isgreater(a,b):
    if(a>b):
        print('a is greater')
    else:
        print('b is greater')

def islesser(a, b):
    if(a<b):
        print('a is smaller than b')
    else:
        print('b is smaller than a')

a=19
b=12
gmean(a,b)#This is called function call
isgreater(a,b)#This is called function call)
islesser(a,b)