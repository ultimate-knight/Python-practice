here we learn about format string#
letter="my name is {} and i'm from {}"; 
letter="my name is {0} and i'm from {1}";#u can even put numbers in flower brackets if u want the arguments in format to be printed in sequence#
letter="my name is {{0} and i'm from {1}}";#when we added extra flower bracket before and after the starting and the ending flower bracket we basically want the interpreter to print those arguments without being converted to other data#
name='maaz';
country='india';
pocket=90.7890;
txt=letter.format(name, country);#what happened here is when we put flower brackets in letter variable which has string those brackets were occupied by the arguments of format method#
print(letter.format(name, country));
print(txt);
print(letter);
print(f"my name is {name} and i'm from {country}");#what happened here is when we use f'string this string allows u to define those arguments from format directly in the string sentence u don't have to use another line to format a string#
print(f"i have {pocket:.2f} rupees");#what happens is suppose if u declare a variable with number along with decimal then when u interpolate that variable as f string with setting variable to 1f 2f or and f it will print the decimal of specified number f if 2f is interpolated it will print number with 2 decimal don't forget to apply . before f like these .2f"#
print(f"{2*30}");#what happened here is when we added numbers in {} brackets it gives us the value in string#