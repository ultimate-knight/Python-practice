#here we study about Lists#
# List=[34,45,56,78, 'maaz'];
# print(List);
# print(List[0]);
# print(List[1]);
# print(List[3]);
# print(List[-4]);

# if 45 in List:
#     print('yes')
# else:
#     print('no');
     

# if 'aa' in 'maaz':
#     print('yes')
# else:
#     print('no');
    
    
    
# print(List[2:5]);
# print(List[1:]);
# print(List[1:3]);#if we write it starts from 1 index and upon reaching 3rd index it subtracts to 3-1 which gives 2.So it gives last number as 2nd index#
# print(List[1:3:2]);#we call this as jumping index it the last number 2.what it does it jumps suppose 1,2,3,4 are in list 1,3 is printed because it jumps from 1,2 then it reaches 3 as there enough values after 3 it won't jump.

lst=[i*i for i in range(10) if(i%2==0)]
print(lst);
