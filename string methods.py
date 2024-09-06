#Strings are immutable
str1='maaz  jackson  is  maaz';
print(len(str1));#it provides the length of string#
print(str1.replace('maaz', 'benry'));#it replace one string in the sentence with the other#
print(str1.lower());#it converts every capital letter to small letter#
print(str1.upper());#it converts every small letter to capital letter#
print(str1.rstrip('y'));#it removes the last character or item from the string#
print(str1.split(' '));#if there are white spaces between the string it will split the string with commas creating a list#
print(str1.capitalize())#Make the first letter of string in sentence to capital letter#
print(str1.center(23));#it will drag string into the center by adding 23 spaces before it#
print(len(str1));
print(len(str1.center(23)));#
print(str1.count('maaz'));#it will check how many maaz string in the sentence str1#
print(str1.find('jackson'));#it will return the index number of jackson in sentence of str1#
print(str1.endswith('maaz'));#it will check wrether the string ends with maaz or not using boolean true or false#
print(str1.startswith('maaz'));#same as above line but opposite#
print(str1.index('jackson'));#it will return the index first index number of jackson character#
print(str1.isalnum());#it will check wrether there is a-z A-Z or 1-9 in the string it return true if there is no punctuation or any other craracter like space#
print(str1.isalpha());#it will return true if the entire string is alphabets#
print(str1.isprintable());#it checks wrether the string is capable of being printed#
print(str1.isspace());#it checks whether there is empty space in string#
print(str1.swapcase());#here  it swaps uppercase to lower and lower case to upper#
print(str1.title());#in a str1 it will convert every first character in a string to capital letter#