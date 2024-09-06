#these are for practice#
# class specifier:
#     def __init__(self):
#         self.name='maaz'
#         print(f"{self.name}")
#     # def __init__(self, name, age, rollno):
#     #     self.__name=name
#     #     self.__age=age
#     #     self.__rollno=rollno
        
# # a=specifier('maaz', 22, 35)
# # print(a._specifier__name)
# # print(a._specifier__age)
# # print(a._specifier__rollno)

# a=specifier()
# print(a)



#     def __init__(self):
#         self._name='maaz'
#         self._age=22
        
        
# class employee(specifier):
#     pass
    
# a=specifier()
# b=employee()
# print(a._name)
# print(a._age)
# print(b._age)
# print(b._name)



#This is async function#
# import requests
# import time
# import asyncio

# async def func1():
#     url='https://cdn.britannica.com/49/182849-050-4C7FE34F/scene-Iron-Man.jpg'
#     response=requests.get(url, allow_redirects=True)
#     open('naukri9.png', 'wb').write(response.content)
#     # time.sleep(3)
#     print('func1 is printed')
#     return func1
 
# async def func2():
#     url='https://cf-images.us-east-1.prod.boltdns.net/v1/static/5359769168001/0a823cb0-01a9-4835-a348-c64187783ccb/d37cb96c-805c-4aa2-9f2f-e62d9eb814c7/1280x720/match/image.jpg'
#     response=requests.get(url, allow_redirects=True)
#     open('naukri6.png', 'wb').write(response.content)
#     # time.sleep(3)
#     print('func2 is printed')
#     return func2
   
# async def func3():
#     url='https://static1.srcdn.com/wordpress/wp-content/uploads/2023/02/hulk-in-avengers-age-of-ultron.jpg'
#     response=requests.get(url, allow_redirects=True)
#     open('naukri4.png', 'wb').write(response.content)
#     print('func3 is printed')
#     return func3
    
    
    
# async def main():
#     task=asyncio.create_task(func1())
# #     await func1()
# #     # await func2()
    
    
#     L=await asyncio.gather(
#         func1(),
#         func2(),
#         func3(),
#     )

#     print(L)
        

# asyncio.run(main())




#break and continue#
# for i in range(20):
#     if(i==10):
#         break
#     print('5X', i+1, '=', 5*(i+1))
    
# for i in range(10):
#     if(i==2):
#         continue
#     print(i)




# class miranda:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
        
#     @classmethod
#     def method(cls, string):
#         return cls(string.split('-')[0], string.split('-')[1] )

# string='harmain-90'
# emp=miranda('maaz', 22)
# print(emp.name)
# print(emp.age)
# emp=miranda.method(string)
# print(emp.name)
# print(emp.age)
    

# class anything:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
        
#     @classmethod
#     def rugby(blas, string):
#         return blas(string.split('-')[0], string.split('-')[1])
    
# string='ribald-24'
# emp=anything('baqtiyaar', 22)
# print(emp.name)
# print(emp.age)
# emp=anything.rugby(string)
# print(emp.name)
# print(emp.age)



# class repository:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
        
    
#     @classmethod
#     def pental(cls, string):
#         name, age=string.split(",")
#         return cls(name, int(age))
    
# emp=repository('baqtiyar', 30)
# print(emp.name)
# print(emp.age)
# emp=repository.pental("maaz, 22")
# print(emp.name)
# print(emp.age)




# class green:
#     company='origin'
    
#     def show(self):
#         print(f"{green.company}")
        
#     @classmethod
#     def present(blaze, changecompany):
#         blaze.company=changecompany
        
# obj=green()
# obj.show()
# # obj.present('amazon')
# green.present('amazon')
# obj.show()



# class repentence:
#     name='maaz'
#     occupation="software engineer"
    
#     def method(self):
#         print(f"hey i'm {self.name} and i'm  working as {self.occupation}")   
# red=repentence()
# red.name='azeez'
# red.occupation='construction worker'
# red.method()
# yellow=repentence()
# yellow.method()



# print("hey i'm \'working here\' for you")
# print("hey be there\n by tomorrow")
# print('hey 90 seconds 45 people')
# print('hey', 90, 'seconds', 45, )



# def greet(fx):
#     def mfx(*args, **kwargs):
#         print('hey man')
#         fx(*args, **kwargs)
#         print('bye')
#     return mfx

# @greet
# def hello():
#     print("hey i'm maaz")
    
# @greet
# def multiply(a, b):
#     print(a*b)
        
# hello()
# multiply(114, 114)




# Dict1={'name': 'maaz', 'age': 22, 'sex': 'male'}
# Dict2={'Nationality': 'indian', 'rollno': 160319733025, 'college': 'deccan'}
# print(Dict1)
# print(Dict2)
# # Dict1.update(Dict2)
# print(Dict1)
# # Dict1.clear()
# # print(Dict1)
# # del Dict1
# Dict1.pop('name')
# print(Dict1)
# Dict1.popitem()
# print(Dict1)
# print(Dict1.keys())
# print(Dict1.values())
# print(Dict1['name'])
# print(Dict1.get('baqtiyar'))
# for key in Dict1.keys():
#     print(key)
#     print(Dict1[key])
#     print(Dict1.items())
    
# for key, value in Dict1.items():
#     print(f"The {key} is {value}")


# x=[12,34,56]
# print(dir(x))
# print(x.__doc__)
# print(help(x))




# class employee:
#     # name='maaz'
#     # age=22
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
# emp=employee('maaz', 22)
# # print(emp.name)
# # print(emp.age)
# print(emp.__dict__)



# def comma(n):
#     '''hey be there by the time be here'''
#     print(n**n)
    
# comma(90)
# print(comma.__doc__)
    



# arr23=[23,45,67,89,90,45]
 
# for index, maerks in enumerate(arr23):
#      print(f"{maerks} in {index}")



# n=int(input('enter a number'))
# print('it is a number')
# try:
#     y=int(input('what is the number'))
# except:
#     print('it is an error')
    
    
    
# f=open('why not practice.txt', 'r')
# txt=f.read()
# print(txt)
# f=open('why not practice.txt', 'a')
# tlt=f.write('\nare u with me how is it going')
# print(tlt)

# with open('why not practice.txt', 'a') as f:
#     f.write("\n don't go with them")




# n=int(input('enter a number'))
# try:#here if error occurs in try the except block get executed#
#     y=int(input('enter a number'))
#     print('it is a number')
# except:
#     print('it is error dude')
# finally:#it will get executed no matter what whether there is error or not#
#     print('really')



# for i in range(10):
#     if(i==4):
#         break
#     print(i)
# else:
#     print('say something')



# naam='mogadishu'
# for i in naam:
#     print(i)
#     if(i=='g'):
#         print('hey there')


        
# reem=['mogadishu', 'cape town', 'islamabad', 'delhi']
# for rent in reem:
#     print(rent)
#     for i in rent:
#         print(i)


# for i in range(2, 89, 9):#it means i=2, i<89, 9++#
#     print(i)



# name='maaz'
# age=22
# print(f"my name is {name} and i'm {age} years old")
    
    
    

# def arg(a=9, b=33):
# def arg(a, b):
    # print(a+b)
# arg(90)#here it will replace a value with 90#
# arg(993, 678)



# def average(*variables):
#     sum=0
#     for i in variables:
#         sum=sum+i
#     print('Average is:', sum/len(variables))
    
# average(90, 89, 78, 67, 55)

# sum=0
# while True:
#     n=int(input('enter a number'))
#     sum+=n
#     print(sum)


# n=int(input('enter a number'))
# for i in range(30):
#     # print('5','X', i+1, '=', 5*(i+1))#This is multiplication table#
#     print(f"{n}X{i+1}=", n*(i+1))


# def average(*variables):
#     sum=0
#     for i in variables:
#         sum=sum+i
#     print('Average is:', sum/len(variables))
# average(12,34,56,78,90)



# def arg2(**variables):
#     print(f"hey", variables['fname'], "and", variables['gname'], "where is", variables['lname'] )#here variables is dictionary whereas fname gname and lname are keys inside dictionary and baqtiyaar amaan and ali is their respective values#
    
# arg2(fname='maaz', gname='amaan', lname='ali')


# import time
# from functools import lru_cache
# @lru_cache
# def fx(n):
#     time.sleep(3)
#     print(n*7)
 
# fx(20)
# print('done after 20')
# fx(30)
# print('done after 30')
# fx(40)
# print('done after 40')
# fx(50)
# print('done after 50')

# fx(20)
# print('done after 20')
# fx(30)
# print('done after 30')
# fx(40)
# print('done after 40')
# fx(50)
# print('done after 50')





# n=int(input('enter a number'))
# if(n==3):
#     print('it is prime')
# elif(n%3==0):
#     print('it is not prime')
# elif(n==2):
#     print('it is prime')
# elif(n==5):
#     print('it is prime')
# elif(n%2==0):
#     print('it is not prime')
# elif(n%5==0):
#     print('it is not prime')
# elif(n==7):
#     print('it is prime')
# elif(n==11):
#     print('it is prime')
# elif(n%11==0):
#     print('it is not prime')
# elif(n%7==0):
#     print('it is not prime')
# else:
#     print('it is prime')
            

# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# n = int(input('Enter a number: '))

# if is_prime(n):
#     print('It is prime')
# else:
#     print('It is not prime')


# def is_prime(n):
#     if n<=1:
#         return False
    
#     if n==2:
#         return True
    
#     if n%2==0:
#         return False
    
    
#     for i in range(3, int(n**0.5)+1, 2):
#         if n%i==0:
#             return False
#     return True
# n=int(input('enter a number'))
# if is_prime(n):
#     print('it is prime')
# else:
#     print('it is not prime')
        
        
# def mean(a, b):
#     x=a*b/a+b
#     print(x)

# mean(90,34)


# def isgreater(a,b):
#     if(a>b):
#         print('a is greater')
#     else:
#         print('b is greater')
# isgreater(23, 78)




# def my_gen():
#     for i in range(9):
#         yield i
# gen=my_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# n=int(input('enter a number'))
# def factorial(n):
#     if(n==0 or n==1):
#         print(1)
#     else:
#         print(n*n-1)
        
# factorial(n)
    
    
# n=int(input('enter a number'))
# def fibonacci(n):
#     if(n==0 or n==1):
#         print(1)
#     else:
#         print(n+n-1+n-1)
# #     else:
# #         n=n+n-1+n-2
# #         n-=1
# #         print(n)

# # fibonacci(n)
# fibonacci(n)


# def fibonacci(n):
#     a, b = 0, 1
#     sequence = []
#     while n > 0:
#         sequence.append(a)
#         a, b = b, a + b
#         n -= 1
#     return sequence

# n = int(input('Enter the number of terms: '))
# print(fibonacci(n))




# def fibonacci(n):
#     a, b=0, 1
#     sequence=[]
#     while n>0:
#         sequence.append(a)
#         a, b=b, a+b
#         n-=1
#     return sequence
    
# n=int(input('enter a number'))
# print(fibonacci(n))



# class letter:
#     def __init__(self, value):
#         self._value=value
        
#     def show(self):
#         print(f"value is {self._value}")
    
#     @property
#     def ten_value(self):
#         return 10*self._value
        
#     @ten_value.setter
#     def ten_value(self, new_value):
#         self._value=new_value
        
# sent=letter(10)
# sent.show()
# # sent.ten_value=67
# print(sent.ten_value)
        



# import time
# name=input('enter a name')
# timestamp=time.strftime("%H:%M:%S")
# print(timestamp)
# h=int(time.strftime('%H'))
# if(h>4, h<12):
#     print('good morning', name)
# elif(h<4, h>12):
#     print('good afternoon', name)
# else:
#     print('good evening', name)
    


# class Animal:
#     def show(self):
#         print('my name is maaz')
        
# class cam(Animal):
#     def vent(self):
#         print('how dare u bark')
        
# class van(Animal):
#     def zenda(self):
#         print('remember me')
        
# obj1=van()
# obj2=cam()
# obj2.show()
# obj2.vent()
# obj1.show()
# obj1.zenda()



# class Human:
#     def walk(self):
#         print('can u walk')
        
# class Animal(Human):
#     def run(self):
#         print('can u run')
        
# class wingedanimal:
#     def animal(self):
#         print('are u winged animal')
        
# class runner(wingedanimal, Animal):
#     def sprint(self):
#         print("let's sprint")
        

# run=runner()
# run.walk()
# run.run()
# run.animal()
# run.sprint()


# n=(input('enter a number'))
# def is_palindrome(n):
#     if(n[1:]==n[:-1]):
#         print('it is palindrome')
#     else:
#         print('it is not')
        
# is_palindrome(n)



# n=int(input('enter a number'))
# def power_of_3(n):
#     if n<=1:
#         return None
#     if(n//3):
#         print('it is power of 3')
#     else:
#         print('it is not')
# power_of_3(n)
        

# class hex:
#     name='maaz'
    
# class desk:
#     def __init__(self, age, value):
#         self.age=age
#         self.value=value
        
#     def show(self):
#         print(f"hey it's {self.age} and my salary is {self.value}")
        

# obj1=hex()
# print(obj1.name)
# obj1.name='baqtiyar'
# print(obj1.name)
# obj2=desk(22, 34000)
# obj2.show()


# a=[1,2,4,5]
# b=[1,2,4,5]
# c=90
# d=90
# print(a is b)
# print(a==b)
# print(c is d)
# print(c==d)


# def temp_celsius_to_farhenheit(celsius):
#     return (celsius*9/5)+32

# celsius=[23, 45, 32, 18]
# celsius_to_fahrenheit=map(temp_celsius_to_farhenheit, celsius)
# fahrenheit_list=list(celsius_to_fahrenheit)
# print(fahrenheit_list)


# def sqrt(n):
#     return n**0.5

# n=[32, 45, 67, 89, 90, 98]
# square=map(sqrt, n)
# list=list(square)
# print(list)


# def even_number(m):
#     return m%2==0
# even=[23,44, 64, 32, 98, 88, 24, 38, 12, 19, 90, 67, 59, 30, 42]
# filtrate=filter(even_number, even)
# list=list(filtrate)
# print(list)



# cube=lambda x,y: x+y
# square=lambda x,y: x**y
# root=lambda x,y: x%y
# print(cube(23, 43))
# print(square(3, 7))
# print(root(45, 3))



# l=[23, 45, 67, 78, 89, 90, 34, 45, 12, 29, 38, 47, 58, 70]
# # l.sort()
# # l.reverse()
# # l.sort(reverse=True)
# m=l.copy()
# # print(l)
# # print(m)
# # print(m.count(23))
# # print(m.index(12))
# # m[0]=22
# # print(m)
# # m.insert(2, 788)
# # print(m)
# z=[334, 565, 787, 908]
# m.extend(z)
# print(m)



# def max_arr():
#     arr=[23, 78, 90, 67, 56, 45]
#     print(max(arr))
        
# max_arr()


# def sum_arr():
#     arr=[34, 56, 67, 89, 90]
#     sum=0
#     for i in arr:
#         sum+=i
#     print(sum)
    
# sum_arr()


# def reverse_arr():
#     arr=[12, 34, 56, 78, 90, 98, 780]
#     arr.reverse()
#     print(arr)
    
# reverse_arr()


# list=[12, 45, 56, 78, 90, 34]
# print(list[1])
# print(list[3])
# print(list[2:])
# print(list[-2:])
# print(list[2:6])

# if 'aa' in list:
#     print('yes')
# else:
#     print('no')
    
# if 12 in list:
#     print('yes')
# else:
#     print('no')







# def find_duplicates():
#     a = [90, 56, 45, 34, 78, 52, 52]
#     if not a:
#         return None

#     sort_a = sorted(a)
#     for i in range(len(sort_a) - 1):
#         if sort_a[i] == sort_a[i + 1]:
#             print('duplicate found')
#             return True
#     print('not found')
#     return False



    
    
    
    
    

# l=[i*i*i for i in range(9) if(i%3==0)]
# print(l)



# #global variables and local variables#
# x=9

# def method():
#     global x
#     x=90
    
# print(x)
# method()
# print(x)



# class objects:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
        
#     def __str__(self):
#         return f"My name is {self.name} and my age is {self.age}"
    
#     def __repr__(self):
#         return f"name={self.name} age={self.age}"
    
#     def __call__(self, value):
#         return self.age+value
    
#     def __len__(self):
#         return len(self.name)
    
# instance=objects('maaz', 22)
# print(instance.__str__())
# print(instance.__repr__())
# print(instance.__call__(23))
# print(instance.__len__())


# from functools import reduce
# l=[23, 34, 56, 12, 43]
# # def lisbon(x,y):
# #     return x*y
# def cube(x):
#     return x*x*x

# def func34(x):
#     return x>34
# # rip=reduce(lisbon, l)
# # print(rip)
# rem=list(map(cube, l))
# print(rem)


# x=int(input('enter a number'))

# match x:
#     case 3:
#         print('it is 3')
        
#     case 5:
#         print('it is 5')
        
#     case 10:
#         print('it is 10')
        
#     case 20:
#         print('it is 20')
        
#     case _ if x!=90:
#         print('it is not 90')
        
       
        
# class Animal:
#     def __init__(self, name):
#         self.name=name
#         print(f"This is animal initializer: {self.name}")
        
# class dog(Animal):
#     def __init__(self, name, breed):
#         self.breed=breed
#         super().__init__(name)
#         print(f'the name of the breed is {self.breed}')
        
# rant=dog('puppy', 'rottweiler')
# rant
        




# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor

# def gimme(seconds):
#     print(f"give me {seconds} seconds")
#     time.sleep(3)

# def ref():
#     for i in range(6):
#         print(f"thread is {i}")
        
# def peep():
#     Ant=['monkey', 'tiger', 'lion', 'elephant']
#     for i in Ant:
#         print(f"Animal name is {i}")
# time1=time.perf_counter()  
# thread1=threading.Thread(target=ref())
# thread2=threading.Thread(target=peep())
# thread3=threading.Thread(target=gimme, args=[5])
# thread4=threading.Thread(target=gimme, args=[8])


# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()

# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()

# time2=time.perf_counter()
# time=time2-time1
# print(time)

# print('threads are completely executed')

# def poolingdemo():
#     with ThreadPoolExecutor as executor:
#         future1=executor.submit(gimme, 8)
#         future2=executor.submit(gimme, 9)
#     print(future1.result)
#     print(future2.result)





# import multiprocessing
# import concurrent.futures
# import requests

# def main(url, name):
#     print(f"process started {name}")
#     response=requests.get(url)
#     open(f'hemanuric{name}.png', 'wb').write(response.content)
#     print(f'process completed {name}')
    
# url='https://picsum.photos/2000/3000'
# pros=[]

# for i in range(60):
#     if __name__=='__main__':
#         process=multiprocessing.Process(target=main, args=[url, i])
#         process.start()
#         pros.append(process)
    
# for process in pros:
#     process.join()


# def generate_primes(n):
#     is_prime = [True] * (n + 1)
#     is_prime[0] = is_prime[1] = False
    
#     p = 2
#     while p * p <= n:
#         if is_prime[p]:
#             for i in range(p * p, n + 1, p):
#                 is_prime[i] = False
#         p += 1
    
#     primes = [p for p in range(2, n + 1) if is_prime[p]]
#     return primes

# n=int(input('enter a number'))
# print(f"Prime numbers from 1 to {n}:", generate_primes(n))

# import heapq
# def find_kth_largest(nums, k):
#     return heapq.nlargest(k, nums)[-1]

# print(find_kth_largest([3,4,5,7,8,9],3))



# def find_mex(arr):
#     """Function to find the MEX of the array."""
#     present = set(arr)
#     mex = 0
#     while mex in present:
#         mex += 1
#     return mex

# def min_removals_to_change_mex(arr):
#     """Function to find the minimum number of removals needed to change the MEX."""
#     original_mex = find_mex(arr)
#     print(f"Original MEX: {original_mex}")
    
#     # If the original MEX is 0, removal of elements may not change it.
#     if original_mex == 0:
#         if 0 in arr:
#             return 1  # Remove one occurrence of 0 to potentially change the MEX
#         else:
#             return -2  # Not possible to change the MEX if 0 is not in the array

#     # Count occurrences of each number
#     from collections import Counter
#     counter = Counter(arr)
#     print(f"Counter: {counter}")
    
#     # Try removing elements to change MEX
#     for num in range(original_mex + 1):
#         if num in counter:
#             new_mex = find_mex([x for x in arr if x != num])
#             print(f"Trying to remove {num}, New MEX: {new_mex}")
#             if new_mex != original_mex:
#                 return 1  # If removing one occurrence of this number changes MEX
    
#     # Check if removing exactly 2 elements can change the MEX
#     for num1 in range(original_mex + 1):
#         for num2 in range(num1 + 1, original_mex + 1):
#             if num1 in counter and num2 in counter:
#                 new_mex = find_mex([x for x in arr if x != num1 and x != num2])
#                 print(f"Trying to remove {num1} and {num2}, New MEX: {new_mex}")
#                 if new_mex != original_mex:
#                     return 2  # If removing these two different numbers changes MEX
    
#     # Check if removal of all occurrences of original_mex is needed
#     if original_mex in counter:
#         return counter[original_mex]  # Remove all occurrences of the MEX
    
#     return -2  # If no valid removal found

# # Read input
# if __name__ == "__main__":
#     try:
#         size = int(input().strip())
#         array = list(map(int, input().strip().split()))
#         print(f"Input array: {array}")
        
#         # Calculate minimum removals needed to change the MEX
#         result = min_removals_to_change_mex(array)
        
#         # Print the result
#         print(result)
#     except Exception as e:
#         print(f"An error occurred: {e}")


# min_removals_to_change_mex(arr)


# def find_mex(arr):
#     """Function to find the MEX of the array."""
#     present = set(arr)
#     mex = 0
#     while mex in present:
#         mex += 1
#     return mex

# def min_removals_to_change_mex(arr):
#     """Function to find the minimum number of removals needed to change the MEX."""
#     original_mex = find_mex(arr)
    
#     # If the original MEX is 0, removal of elements may not change it.
#     if original_mex == 0:
#         return 1 if 0 in arr else -1  # Changed -2 to -1 for consistency

#     # Count occurrences of each number
#     from collections import Counter
#     counter = Counter(arr)
    
#     # Try removing elements to change MEX
#     for num in range(original_mex + 1):
#         if num in counter:
#             new_mex = find_mex([x for x in arr if x != num])
#             if new_mex != original_mex:
#                 return 1  # If removing one occurrence of this number changes MEX
    
#     # Check if removing exactly 2 elements can change the MEX
#     for num1 in range(original_mex + 1):
#         for num2 in range(num1 + 1, original_mex + 1):
#             if num1 in counter and num2 in counter:
#                 new_mex = find_mex([x for x in arr if x != num1 and x != num2])
#                 if new_mex != original_mex:
#                     return 2  # If removing these two different numbers changes MEX
    
#     # Check if removal of all occurrences of original_mex is needed
#     if original_mex in counter:
#         return counter[original_mex]  # Remove all occurrences of the MEX
    
#     return -1  # Changed -2 to -1 for consistency

# # Read input
# if __name__ == "__main__":
#     size = int(input().strip())
#     array = list(map(int, input().strip().split()))
    
#     # Calculate minimum removals needed to change the MEX
#     result = min_removals_to_change_mex(array)
    
#     # Print the result
#     print(result)




# def count_flipped_bits(P, Q, R):
#     # Convert P, Q, and R to binary strings
#     bin_P = bin(P)[2:]
#     bin_Q = bin(Q)[2:]
#     bin_R = bin(R)[2:]
    
#     # Pad the binary strings to make them of equal length
#     max_len = max(len(bin_P), len(bin_Q), len(bin_R))
#     bin_P = bin_P.zfill(max_len)
#     bin_Q = bin_Q.zfill(max_len)
#     bin_R = bin_R.zfill(max_len)
    
#     # Calculate P XOR Q
#     xor_result = int(bin_P, 2) ^ int(bin_Q, 2)
#     bin_xor_result = bin(xor_result)[2:].zfill(max_len)
    
#     # Count the number of differing bits between bin_xor_result and bin_R
#     flips_needed = 0
#     for bit_xor, bit_r in zip(bin_xor_result, bin_R):
#         if bit_xor != bit_r:
#             flips_needed += 1
    
#     return flips_needed

# # Input
# P = int(input())
# Q = int(input())
# R = int(input())

# # Output
# print(count_flipped_bits(P, Q, R))



# def min_removals_to_change_mex(n, A):
#     # Determine the current MEX of the array
#     present = [False] * 91
#     for num in A:
#         if num <= 90:
#             present[num] = True
    
#     mex = 0
#     while mex <= 90 and present[mex]:
#         mex += 1
    
#     if mex == 91:
#         return -2
    
#     # To change the MEX, remove all occurrences of mex or ensure all numbers 0 to mex-1 are present
#     if mex > 0:
#         count_mex = A.count(mex)
#         missing_elements = sum(1 for i in range(mex) if not present[i])
#         return min(count_mex, missing_elements)
#     else:
#         return A.count(0)

# # Input
# n = int(input())
# A = list(map(int, input().split()))

# # Output
# print(min_removals_to_change_mex(n, A))

# def min_removals_to_change_mex(n, A):
#     # Determine the current MEX of the array
#     present = [False] * 91
#     for num in A:
#         if num <= 90:
#             present[num] = True
    
#     mex = 0
#     while mex <= 90 and present[mex]:
#         mex += 1
    
#     if mex == 91:
#         return -2
    
#     # To change the MEX, remove all occurrences of mex or ensure all numbers 0 to mex-1 are present
#     if mex > 0:
#         count_mex = A.count(mex)
#         missing_elements = sum(1 for i in range(mex) if not present[i])
#         return min(count_mex, missing_elements)
#     else:
#         return A.count(0)

# # Test case 1
# n1 = 4
# A1 = [0, 1, 1, 4]
# print(min_removals_to_change_mex(n1, A1))  # Expected output: 1

# # Test case 2
# n2 = 3
# A2 = [2, 4, 11]
# print(min_removals_to_change_mex(n2, A2))  # Expected output: -2



# def calculate_mex(arr):
#     mex = 0
#     present = set(arr)
#     while mex in present:
#         mex += 1
#     return mex

# def min_removals_to_change_mex(A):
#     n = len(A)
#     original_mex = calculate_mex(A)
    
#     # If MEX is already greater than the maximum element, we can't increase it
#     if original_mex > max(A):
#         return -1
    
#     # Count the occurrences of each number
#     count = {}
#     for num in A:
#         count[num] = count.get(num, 0) + 1
    
#     removals = 0
    
#     # Remove elements equal to MEX until we can increase it
#     while original_mex in count:
#         removals += 1
#         count[original_mex] -= 1
#         if count[original_mex] == 0:
#             del count[original_mex]
#             return removals
    
#     return removals

# # Read input
# n = int(input())
# A = list(map(int, input().split()))

# # Calculate and print the result
# result = min_removals_to_change_mex(A)
# print(result)




# def calculate_mex(arr):
#     mex = 0
#     present = set(arr)
#     while mex in present:
#         mex += 1
#     return mex

# def min_removals_to_change_mex(A):
#     n = len(A)
#     original_mex = calculate_mex(A)
    
#     # If MEX is already the maximum possible value, we can't increase it
#     if original_mex == 91:  # Since 0 <= A[i] <= 90
#         return -1
    
#     # Count the occurrences of each number
#     count = {}
#     for num in A:
#         count[num] = count.get(num, 0) + 1
    
#     removals = 0
    
#     # Try removing elements to change MEX
#     if original_mex in count:
#         removals = count[original_mex]
#     else:
#         # If original_mex is not in the array, we need to remove all elements smaller than it
#         for num in range(original_mex):
#             if num in count:
#                 removals += count[num]
    
#     return removals if removals < n else -1

# # Read input
# n = int(input())
# A = list(map(int, input().split()))

# # Calculate and print the result
# result = min_removals_to_change_mex(A)
# print(result)



# def count_bits_to_flip(P, Q, R):
#     # Compute P XOR Q
#     xor_PQ = P ^ Q
    
#     # Compute XOR result with R
#     xor_result = xor_PQ ^ R
    
#     # Count the number of 1s in the binary representation of xor_result
#     return bin(xor_result).count('1')

# # Read inputs
# P = int(input().strip())
# Q = int(input().strip())
# R = int(input().strip())

# # Calculate and print the result
# print(count_bits_to_flip(P, Q, R))



# def calculate_total_amount(denominations):
#     # Denomination values in cents
#     values = [20, 40, 100, 200, 500, 1000]
    
#     # Calculate the total amount in cents
#     total_cents = sum(denominations[i] * values[i] for i in range(6))
    
#     # Convert cents to dollars
#     total_dollars = total_cents / 100.0
    
#     # Return the total amount rounded to 1 decimal place
#     return round(total_dollars, 1)

# # Read input
# denominations = list(map(int, input().strip().split()))

# # Calculate and print the total amount
# print(calculate_total_amount(denominations))






# def create_zigzag(s, n):
#     if n == 1:  # If the width is 1, the pattern is just the original string
#         return s
    
#     # Create a list of empty strings for each row
#     zigzag = ['' for _ in range(n)]
#     row, step = 0, 1
    
#     for char in s:
#         zigzag[row] += char
#         if row == 0:
#             step = 1
#         elif row == n - 1:
#             step = -1
#         row += step
    
#     # Combine characters from all rows
#     return ''.join(zigzag)

# # Read input
# s = input().strip()
# n = int(input().strip())

# # Create zig-zag pattern and print the result
# password = create_zigzag(s, n)
# print(password)



# def find_special_word(input_string):
#     words = input_string.split()
    
#     # Initialize variables to track the special word
#     special_word = ""
#     max_distinct_count = 0
    
#     for word in words:
#         # Count distinct letters in the word
#         distinct_letters = set(word)
#         distinct_count = len(distinct_letters)
        
#         # Update the special word based on the conditions
#         if (distinct_count > max_distinct_count or
#             (distinct_count == max_distinct_count and word < special_word)):
#             special_word = word
#             max_distinct_count = distinct_count
    
#     return special_word

# # Read input
# input_string = input().strip()
# # Find and print the special word
# print(find_special_word(input_string))





# def classify_numbers(array, threshold):
#     larger = []
#     smaller = []
    
#     for num in array:
#         if num > threshold:
#             larger.append(num)
#         elif num < threshold:
#             smaller.append(num)
    
#     return larger, smaller

# # Read input
# size = int(input().strip())
# array = list(map(int, input().strip().split()))
# threshold = int(input().strip())

# # Classify numbers and get results
# larger, smaller = classify_numbers(array, threshold)

# # Print results
# print("Larger:", ' '.join(map(str, larger)))
# print("Smaller:", ' '.join(map(str, smaller)))




# def calculate_total_energy(M, R, N):
#     # Total energy produced over N seconds
#     total_energy = N * M + R * (N * (N - 1)) // 2
#     return total_energy

# # Read input
# M = int(input().strip())
# R = int(input().strip())
# N = int(input().strip())

# # Calculate and print the total energy
# print(calculate_total_energy(M, R, N))


# def count_frequencies(text):
#     # Initialize a list to store frequencies of letters a-z
#     frequency = [0] * 26
    
#     # Count frequencies
#     for char in text:
#         frequency[ord(char) - ord('a')] += 1
    
#     # Construct the output string
#     result = []
#     for i in range(26):
#         if frequency[i] > 0:
#             result.append(chr(i + ord('a')) + str(frequency[i]))
    
#     return ''.join(result)

# # Read input
# text = input().strip()

# # Compute and print the frequency count
# print(count_frequencies(text))




# def combine_scores(chemistry_scores, english_scores):
#     # Convert the comma-separated strings to lists of integers
#     chemistry_list = list(map(int, chemistry_scores.split(',')))
#     english_list = list(map(int, english_scores.split(',')))
    
#     # Combine the scores into a list of tuples
#     combined_scores = list(zip(chemistry_list, english_list))
    
#     return combined_scores

# # Read input
# chemistry_scores = input().strip()
# english_scores = input().strip()

# # Combine scores and get the result
# result = combine_scores(chemistry_scores, english_scores)

# # Print the result
# for scores in result:
#     print(f"{scores[0]},{scores[1]}")





# def is_subset(a, b):
#     return a.issubset(b)

# # Read number of test cases
# T = int(input().strip())

# for _ in range(T):
#     # Read and parse set A
#     num_elements_A = int(input().strip())
#     elements_A = set(map(int, input().strip().split()))
    
#     # Read and parse set B
#     num_elements_B = int(input().strip())
#     elements_B = set(map(int, input().strip().split()))
    
#     # Check if A is a subset of B and print the result
#     print(is_subset(elements_A, elements_B))




# def convert_words_to_digits(contact_words):
#     # Mapping of words to digits
#     word_to_digit = {
#         'zero': '0', 'one': '1', 'two': '2', 'three': '3',
#         'four': '4', 'five': '5', 'six': '6', 'seven': '7',
#         'eight': '8', 'nine': '9'
#     }
    
#     # Split input into words
#     words = contact_words.split()
    
#     result = []
#     i = 0
    
#     while i < len(words):
#         word = words[i]
        
#         if word == 'double':
#             digit = word_to_digit[words[i + 1]]
#             result.append(digit * 2)
#             i += 2
#         elif word == 'triple':
#             digit = word_to_digit[words[i + 1]]
#             result.append(digit * 3)
#             i += 2
#         else:
#             # Normal digit or part of a longer sequence
#             result.append(word_to_digit[word])
#             i += 1
    
#     # Join the result list into a single string
#     return ''.join(result)

# # Read input
# contact_words = input().strip()

# # Convert and print the contact number
# print(convert_words_to_digits(contact_words))


# n=int(input('enter a number'))
# def is_prime(n):
#     if n<=1:
#         return False
    
#     if n==2:
#         return True
    
#     if n%2==0:
#         return False
    
#     for i in range(3, int(n**0.5)+1, 2):
#         if n%i==0:
#             return False
#     return True


# if is_prime(n):
#     print('it is prime')
# else:
#     print('it is not prime')
    
    
    
    
# with open('write.txt', 'r') as file:
#     release=file.read()
#     print(release)
#     print(file(count))
    
    
    
# n=str(input('enter a string'))
# def is_palindrome(n):
#     if n==n[::-1]:
#         print('it is palindrome')
#     else:
#         print('no it is not')

# is_palindrome(n)



# import re
# text="hey man good morning my email is maaz2607@gmail.com"
# pattern=r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
# list=re.findall(pattern, text)
# print('the email is:', list)


# import re
# text='hey there live a good life with kersky@gmail.com'
# pattern=r"[A-Za-z0-9%._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
# list=re.findall(pattern, text)
# print(list)



# import time
# t=time.localtime()
# format=time.strftime("%Y-%M-%D %H-%M-%S",t)
# print(format)


# range=[i**2 for i in range(11)]
# print(range)



# try:
#     n=int(input('enter a number'))
#     if(n/0==0):
#         print('it is valid')
# except:
#     print('it is not valid')
    
       
# even=[1,23,45,67,89,24,56,88,98,56,12,44] 
# def func(even):
#     return even**3

# odd=map(func, even)
# rist=list(odd)
# print(rist)



# def gen():
#     for i in range(5):
#         yield(i)
        
# best=gen()
# print(next(best))
# print(next(best))
# print(next(best))
# print(next(best))





# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor

# def func(seconds):
#     print(f"it takes {seconds} seconds")
#     time.sleep(seconds)
    
# func(2)
# func(6)
# func(7)

# time1=time.perf_counter()
# t1=threading.Thread(target=func, args=[4])
# t2=threading.Thread(target=func, args=[7])
# t3=threading.Thread(target=func, args=[10])

# t1.start()
# t2.start()
# t3.start()
# time2=time.perf_counter()
# print(time2-time1)

# def poolingdemo():
#     with ThreadPoolExecutor() as executor:
#         future1=executor.submit(func, 3)
#         future2=executor.submit(func, 6)
#         future3=executor.submit(func, 7)
#     print(future1.result())
#     print(future2.result())
#     print(future3.result())
    
# poolingdemo()



import multiprocessing
import time
import concurrent.futures


def downloadfile(url, name):
    









    