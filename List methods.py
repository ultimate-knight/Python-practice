#here we study about the types of method lists in python#
l=[45, 56, 78, 98, 34];
l.sort();#It will sort the list from ascending to ascending#
l.append(102);#it will add new elements to lists#
l.sort(reverse=True);#it will sort the elements from descending to ascending order#xx
l.reverse();#it will reverse items in lists#
print(l.count(56));#it will count the number of items the value appears in list#
print(l.index(78));#it will print the index of the specific number#
m=l.copy();#it will copy all the elements from l to m so new m list is created#
m[0]=90;#it will assign 90 at zero index in m list#
print(l);
print(m);
l.insert(2, 788);#it will replace 2nd index or any index number with 788 or any number#
print(l);
k=[23,46,92,104];
l.extend(k);#it will add the elements of k in l list#
print(l);