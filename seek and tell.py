#here we learn about seek and tell functions#
 
with open('write.txt', 'w') as f:#with func function ensures is used to manage the function to make sure the function opens and close appropriately#
    # f.seek(15)#seek function allows us to start at any index index in the string it provides which index to start from#
    f.write('hello world hey man')#it allows us to add sentence to the file.u can add any sentence to the file using write function#
    # f.truncate(10)#truncate function allows us to cut the size of file to 5 bits if it is of any length and gets printed
    # gata=f.write('my name is maaz')
    # print(gata)
    with open('write.txt', 'r') as f:
        print(f.read())#read function allows us  to read the contents from the file and and fetch those content to the interpreter for printing#
    # print(f.tell())#tell function tells at what position our pointer is right now in a string i mean at what index#