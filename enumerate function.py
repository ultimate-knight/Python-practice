#here we learn about enumerate function#
arr1=[34,56,78,98,23,12]
for i in range(len(arr1)):
index=0
for i in arr1:
    # print(i)#
    print(i)
    # if(index==3):
    #     print('nothing')
    #     index+=1
    # if
    if(index==3):
        print('nothing')
    index+=1
    
#enumerate function return both the index and the value of the lists tuple or string#
for index, marks in enumerate(arr1):
    print(marks)
    if(index==3):
        print('hey man')