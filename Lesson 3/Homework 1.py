"""
Modules-
    packadges/libaries
    they are code that has been created
    with functions that can be used to make life easier
    import()


"""
#import math
#this is a libray that is already build into python
#lz code
import math


print(math.pow(2, 3)) #output 8

print(math.ceil(5.4)) #prints next whole number i.e 6

import power
print(power.power(2, 3))
#this is using the power folder I created, importing the funtion and using it here
#itertools , collections, cmath, math

"""
    functions
    block of code that does stuff
    sectioned, scoped, takes input, and may/may not return value
    ex. print, input, pow, int, str, fromat, center, ljust, rjust,

    key words
        def * **
"""

def example(): #functions defined
    print("Hello world!")

example()

def test(x, y):#these are parameters
    print(x**y) #a subroutine

test(2, 2)#this is the argument

def func(name, age):
    return(name, age)

print(func("John", 2))

def default(name="", age=0):
    return name, age
print("\ncalling default")
print(default())

"""
    args - arguments


    kwargs - keyword arguments
"""
def basic_arguments(computer, shoe):
    print(computer, shoe)
print(basic_arguments('laptop', 'snadles'))

def arguments(*args):
    for arg in args:
        print(arg)
arguments('sdf', 'asdfadsdd')

def basic_keywords(fruit, action):
    print(fruit, action)

basic_keywords(action="run", fruit="pineapple")

def keywords(**kwargs):
    for key, value in kwargs.items():
        print (key, value)
keywords(a="apple", b="banana", c="cherry")

"""
    file input/output
    open, close, readline, read, write
    open- open the file, ready to stream

"""
 f= open('inpur.txt', 'r')
#input.txt is directory and location of file
#'r' is what you want ot do with file (read, "w" write, "r+" read/write)
print("reading file")
print(f.read())
f.close()

write_file= open('inpur.txt', 'w')
write_file= ('\nAnuthuh line')
write_file.close()

f= open('input.txt', 'r')
print("\nopening again")
print(f.read())
f.close
