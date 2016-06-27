"""
    modules

    import, from, as

"""
import math
from math import pow
from math import pow as p
# import django-admin -- third party module
import power
# ** = math.pow(x,y)
print (math.pow(2, 3)) # output 8
print (math.ceil(5.4)) # output 6
print (power.my_pow(3,4)) # output 81

print (pow(2,3)) # output 8.0
print (p(2,3)) # output 8.0

# itertools, collections, cmath, math
"""
    functions

    blocks of code that do stuff
    sectioned, scoped, takes input,
      may or may not return values

    print, input, pow, int, str, format, center,
      ljust, rjust

    def * **
"""
def example():  # function definition
    print ("Hello, World!") # sub

example()

def test(x, y): # parameters
    print (x ** y) # a subroutine

test(2, 2) # arguments

def func(name, age):
    return name, age # function
# public string func(name, age)

print (func("John", 2))

def default(name="", age=0): # default arguments
    return name, age
print("\ncalling default")
print(default())

"""
    args - arguments
    kwargs - keyword arguments
"""

def basic_arguments(computer, shoes):
    print (computer, shoes)

print()
basic_arguments('laptop', 'sandals')

def arguments(*args):
    for arg in args:
        print(arg)

arguments('asdf', '123', 'apple', 'banana', 3, True)

def basic_keywords(fruit, action):
    print(fruit, action)

print()
basic_keywords(action="run", fruit="pineapple")

def keywords(**kwargs):
    for key, value in kwargs.items():
        print (key, value)

print(keywords(a="apple", b="banana", c="cherry",
               action="run"))


"""
    file input/output

    open, close, readline, read, write

    open - open the file and ready to stream

"""

f = open('input.txt', 'r')
# input.txt -- location of file you want to open
# 'r' -- read
# 'w' -- write
# 'a' -- append
# 'r+' -- read/write
print ('reading file')
print (f.read())
f.close()

write_file = open('input.txt', 'w')
write_file.write('\nAnuthuh line')
write_file.close()

append_file = open('input.txt', 'a')
append_file.write('\nhello world i\'m back')
append_file.close()

f = open('input.txt', 'r')
print("\nopening again")
print(f.read())
f.close()

# readline()