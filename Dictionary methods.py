#here we learn about dictionary methods#
dict1={'name': 'maaz', 'age': 22, 'college': 'deccan', 'roll no': 160391733025 }
dict2={'name': 'adnan', 'age': 22, 'college': 'deccan', 'roll no': 160319733027}
dict3={22: 34, 343: 673}
dict4={45: 324, 890: 90}
print(dict1);
dict1.update(dict2);
print(dict1);
print(dict2);
dict3.update(dict4);#
# print(dict3);
dict1.clear();#it will empty the dictionary#
print(dict1);
dict1.pop('name');#here the pop is used to remove any element in a list and u have to provide argument while popping#
dict1.popitem();#it will pop last item in dictionary#
print(dict1);
del dict1;
print(dict1)#here when we use del to delete dictionary it gives when we print dictionary again
When you update dict3 with dict4, since they have different keys, dict3 is expanded to include all key-value pairs from both dictionaries.
When you update dict1 with dict2, since they have the same keys, the values in dict1 are overwritten by the values from dict2.#