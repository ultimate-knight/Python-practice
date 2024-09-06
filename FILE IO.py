#here we learn about files and their operations like read write and append#
f=open('system.txt', "r")
txt=f.read()
print(txt)
f=open('system.txt', "a")
tlt=f.write('being honest')
print(tlt)

with open('system.txt', 'a') as f:
    f.write('help me god') 
