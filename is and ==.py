#here we learn about 'is' and == comparision operator#
a=[1,2,3]#here a and b is false when 'is' comparision operator is used because in lists a and b don't refer to same object especially in lists#
b=[1,2,3]
c=3#here a and b is true in 'is' comparision operator because it is single value a and b which refers to same object#
d=3
print(a is b)
print(a==b)
print(c is d)#is comparision operator checks identity of both variables#
print(c==d)#== comparision operators chceks the values of both variables#