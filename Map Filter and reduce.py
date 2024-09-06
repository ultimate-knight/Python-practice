#here we today study about Map  Filter reduce functions#
from functools import reduce
# def cube(x):
#     return x*x*x

l=[12,34,56,76,89]

def summar(x,y):
    return x*y
    
    

# def lect(x):
#     return x>24#

# lest=list(map(cube, l))#here map function is being used because it is simplifying the procedure whereby it takes first argument as function then it takes any list or tuple or set on which the function is being applied#
# print(lest)

# clest=list(filter(lect, l))
# print(clest)

crest=reduce(summar, l)
print(crest)

