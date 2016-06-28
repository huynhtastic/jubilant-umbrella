"""
   MOdules packages
    files
    standard libraries; someone's ceated before hand with functionality so you can import it

    import
    1) i.e.  math: library thats built into python
"""

# ** = math.pow(x,y)
import math
print (math.pow(2,3))
print (math.ceil(5.4)) #outputs the next bigger integer

#python built in library, itertools, collections. cmath, math

"""
    functions:
    blocks of code that do stuff
        sectioned off, scoped, takes input, may or may not return values
    i.e. print, string, int, format, sensor, ljust, rjust center, input

    in python key words; def    *       **
    def: use to define a funtion in python
"""
def example(): #funtion definition, the header
    print ("Hello World!")#everything inside function is indented

example()

def test(x, y): #paramaters that you want to work with
    print(x ** y) #a subroutine

test(2,2) #arguments are in function, they pass to fulfill function requirements

def func(name, age):
    #in python everything is a function, you don't have to declare
    return name, age # function

print(func("John", 2))

def default(name ="", age =10):
    return name, age
print ("\ncalling default")
print(default())

"""
Two structions called
                    arg - arguments functinoality denoted with (*arg) it unpacks and is one dem.
                    kwargs - short for keyword arguments: you pass into function but have a name
                    don't depend on functional arg. denoted with (**kwargs)
                    only use if you have an unpredictable amount to unpack
"""

def basic_arguments(computer, shoes):
    print(computer, shoes)

basic_arguments('laptop','sandals')

def arguments(*args):
    for arg in args:
        print(args)

arguments('asdf', '123', 'apple', 'banana', 3, True)

def basic_keywords(fruit, action):
    print(fruit, action)

basic_keywords(action = "run", fruit = "pineapple")
def keywords(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print(keywords(a = "apple", b = "bananaPhone", c = "cherries")) #can pass a, b, c for each argument

"""
    file input/output

    open, close, readline, read, write(grab entire file and go though it and put it inside code in order to manipulate)
    open- open file and get ready to stream
"""

f = open('input.txt', 'r')
#input.txt-- location of your file that you want to open
#'r' --read
#'w' -- write
# 'a' = append: don't want to erase anythin in file, just add to it
# 'r+w' -- read/write
#readLine: read line by line
print('reading file')
print (f.read()) #read entire file
f.close()

write_file = open ('input.txt', 'w')
write_file = ('\nAnather line')
write_file.close()

append_file = open('input.txt', 'a')
append_file.write('\hello world i\'m back')
append_file.close()

f = open('input.txt', 'r')
print("\nopening again")
print(f.read())
f.close()