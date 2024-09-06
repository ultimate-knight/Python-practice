#here today we learn about recursion#
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1);

print(factorial(5));
print(factorial(9));
print(factorial(10));        