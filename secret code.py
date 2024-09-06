#here we write secret code#
word=input('do u want to code or decode')
if(word<2):
    word.reverse()
    print(word)
else:
    word.append(random(word[1,3]))
    print(word)