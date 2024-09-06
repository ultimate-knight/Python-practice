user=int(input('enter a number'))

i=1
while(i<=user):
    
    if(i%3==0 and i%5==0):
        print('Fizz buzz')
    elif(i%5==0):
         print('buzz')
    elif(i%3==0):
        print('Fizz')
    else:
        print(i)
    i=i+1
    
    