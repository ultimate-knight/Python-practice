#here we learn about doc-string#
def square(n):
    '''hey be here by the time i see u'''#what's this?well it is a string inserted in between '''string'''.if something is between these commas we call it a doc-string.it can only be defined after function like //def self// it can only be printed when we write //print(function.__doc__)//#
    print(n**2);
    
square(9);
print(square.__doc__);

    