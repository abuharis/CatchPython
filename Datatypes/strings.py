#strings ae packed in quotes assigns to each variable
a, b, c = '123'
print(a,b,c)


#Instead, unpack variable can hold other values, which makes it as a list
a, *b = '1234'
print(a,b)


#string is literally a list of characters or numbers. Able to get the index too
print('Testing'[2])

#since its a list, we could able to loop through
for text in 'I am a python programmer':
    print(text, end='.\n')


#A dictionary format strings can be converted into dict.
tuple = 'a1', 'b1'
print(dict(tuple))


#A variable will be stored in the memory address.
name = "python"
print(id(name))


#string formatting
print(f"{name} is a good programming and the variable is in {id(name)}")


