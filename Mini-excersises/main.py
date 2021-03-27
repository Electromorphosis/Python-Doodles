## exercise 2 (via w3schools.com)

# if 5 > 2:
#    print("Five is more than two")

## exercise 2a

# if 5 > 2:
#    print("""Five is more than
#    two""")

# x=5
# print(x)

## ex. 3

# x = 5
# y = "John"
# print(type(x))
# print(type(y))

'''A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)'''

'''Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"'''

##ex. 4
'''
x = y = z = "Orang"
print(x)
print(y)
print(z)
'''

##ex.5
'''
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
'''

##ex.6
'''
x = "awesome"
print("Python is " + x)
'''
#Further examples:
#String combining
'''
x = "Python is "
y = "awesome"
z =  x + y
print(z)
'''
# For numbers, the + character works as a mathematical operator:
'''
x = 5
y = 10
print(x + y)
'''
# If you try to combine a string and a number, Python will give you an error:
'''
x = 5
y = "John"
print(x + y)
'''

##ex.7 Global variables & functions
'''
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
'''

#local variables:
'''
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
'''
# 'global' keyword can be used for both declaring and changing global variable inside a function

#Data types in python:
'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
'''

#! You cannot convert complex number to another number type !

##ex.8 Random numbers

import random #importing 'random' module

print(random.randrange(1, 10)) #use and set range

