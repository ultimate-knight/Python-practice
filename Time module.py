# #Here we learn about Time module#
import time
# def usingwhile():
#     i=0
#     while i<50000:
#         i=i+1
#         print(i)
        
# def usingfor():
#     for i in range(50000):
#         print(i)
        
# init=time.time()
# usingwhile()
# T1=time.time()-init
# init=time.time()
# usingfor()
# print(T1)
# print(time.time()-init)
        
        
# print(4)
# time.sleep(7)
# print('it is printed after 7 seconds')


t=time.localtime()
formatted_time=time.strftime("%Y-%M-%D %H:%M:%S", t)
print(formatted_time)
    