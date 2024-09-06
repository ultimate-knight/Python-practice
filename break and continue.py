#here we are learning about break and continue#
for i in range(20):
    if(i==20):
        break
    print("5 X", i+1, '=', 5* (i+1) );#Break statement break the loop#
    
    
    
for i in range(12):
    if(i==5):
        continue#it skips the iteration if i there multiples from 1,2,3,4,5 if continue is on 3 then all the multiples will be printed 1,2,4,5 except 3#
    print('5 X', i+1, "=", 5*(i+1));


# The code snippet you provided is an infinite loop using a while loop in Python. It initializes a
# variable `i` to 0 and then enters a loop that will continue indefinitely (`while True:`).

i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break