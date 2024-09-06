#here we learn about dictionaries#
info={"name": 'maaz', "age": 22, 'school': 'kakatiya'};
print(info["name"]);
print(info["age"]);
print(info.get('baqtiyaar'));
print(info.keys());
print(info.values());

for key in info.keys():
    print(info[key]);
    print(key);
    print(f"the value corresponding to {key} is {info[key]}");

print(info.items());


for key, value in info.items():
    print(f"the  value corresponding to {key} is {value}");