We are learning about for loop here#
name='baqtiyaar';
for i in name:
    print(i)
    if(i=='a'):
        print('hey it is me')



names=['maaz', 'baqtiyaar', 'Ali', 'saif']
for name in names:
    print(name)
    for i in name:
        print(i) 


for i in range(1, 89, 2):#here it is like for(i=1; i<89; i++) i++ usually means +1 but here in python we could use +2 like here in (1, 89, 2) 1 is initializing 89 is conditions and 2 is incrementation means it should increment by 2.
    print(i)