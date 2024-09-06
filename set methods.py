#we will learn here about methods of set#
s1={23,44,56,90};
s2={54,89,45,21,11};
s4={23,44};
# print(s1.union(s2));#what happened here is the sets of both s1 and s2 values are printed in one single set it doesn't matter whether they are common or not#
# s1.update(s2);#here the values of s2 which are not in s1 are appended#
# print(s1, s2);#To update a list we have to define like this#
# s3=s1.intersection(s4)#Here it returns the common values in both the sets#
# print(s3)
# # print(s1.symmetric_difference(s4));#here in two sets s1 and s4.All the values which aren't common in s1 and s4 are printed#
# print(s1.isdisjoint(s2));#here what happens is it returns boolean value true or false.if s1 and s2 have common values it returns false.if the values aren't common it returns true.#
# # print(s1.issuperset(s2));
# print(s1.issuperset(s4));#here we call a set a superset when the elements of s4 is present in s1 which is larger set that's how we identify superset#
# print(s4.issubset(s1));  #here we call a set a subset when smaller set values are part of the larger set.If the values of s4 present in s1 we call s4 is subset of s1#    
# s1.discard(23);
# s1.discard(29)#do not print print(s1.remove(29)) like thse,it doesn't work.Always do s1.remove(29) then in second line print this statement print(s1)#
# print(s1); 
# print(s1.pop());#Here the last item is removed from s1.So we don't know what is the last item so any item can be removed because it is unordered#  
# del s1;#it will remove entire set from array#
# print(s1);
# s1.clear();#it will empty the array#
# print(s1);
# if 23 in s1:
#     print('it is always right')#this is conditional statement on set values#
# else:
#     print('it is false')