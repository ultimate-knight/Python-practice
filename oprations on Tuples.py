#here we are learning about operations on Tuples#
# students=('maaz', 'baqtiyaar', 'amaan', 'ali', 'adnan');
# temporary=list(students);#here we are converting tuple to list#
# temporary.pop(3);#we are popping elements from list
# temporary.append('mudassir');#we are adding elements in the list#
# students=tuple(temporary);
# print(students);


# class1=('Apples', 'Oranges', 'Quinoa', 'Watermelon');
# class2=('Tomato', 'potato', 'pumpkin', 'ladyfinger', 'okra');
# class3=class1+class2;#it concatenates the two above strings#
# print(class3);

tuple2=(12, 34, 45, 67, 89, 90, 56, 73, 20,34);
dict=tuple2.index(34);
dict1=tuple2.count(67);
dict2=tuple2.index(34,3,10 );#so here what happening is first the number 34 is value and the next two numbers 3 and 10 in which 3 is the starting index in tuple and 10 is the ending index which is 10-1=9.It finds 34 between 3 index from upto 9th index if they found the value they will return.#
print(dict);
print(dict1);
print(dict2);

