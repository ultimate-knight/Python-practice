#here we are learning about Match cases#
x=int(input('enter a number'));

match x:
    case 3:
        print('it is 3')
    

    case 18:
        print('it is 18')
    

    case 23:
        print('it is 23')

    
    case _ if x!=90:
        print('it is not 90')


    case _ if x!=70:
        print('it is not 80')