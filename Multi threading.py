#here we learn about Multi threading#
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"here we go in {seconds}")
    time.sleep(seconds)

def main():
    # time1=time.perf_counter()    
    func(5)
    func(3)
    func(4)

    t1=threading.Thread(target=func, args=[5])
    t2=threading.Thread(target=func, args=[3])
    t3=threading.Thread(target=func,args=[4] )
    t1.start()
    t2.start()
    t3.start()


    t1.join()
    t2.join()
    t3.join()

    time2=time.perf_counter()
    print(time2-time1)

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1=executor.submit(func, 5)
        future2=executor.submit(func, 3)
        future3=executor.submit(func, 4)
        print(future1.result())
        print(future2.result())
        print(future3.result())
        
        # l=[5,3,4]
        # results=executor.map(func, l)
        # for result in results:
        #     print(result)
    
poolingDemo()


# import threading
# import time

# def print_numbers():
#     for i in range(1, 6):
#         print(f"Number: {i}")
#         time.sleep(1)  # Simulate a delay

# def print_letters():
#     for letter in ['A', 'B', 'C', 'D', 'E']:
#         print(f"Letter: {letter}")
#         time.sleep(1)  # Simulate a delay

# # Create threads
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)

# # Start threads
# thread1.start()
# thread2.start()

# # Wait for both threads to complete
# thread1.join()
# thread2.join()

# print("Both threads have completed their execution.")


