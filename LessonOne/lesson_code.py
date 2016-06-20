"""
    This is code that we went through in class today. I have replicated
    it to the best of my knowledge, but it's not exactly line for line 
    what we did in the first lesson.

    Also, I know my English sucks. Don't judge me Cynthia.

    Topics for Lesson One:
        * Variables
        * Math and Boolean operators
        * Basic I/O (Input/Output)

    Key Items to remember:
        * The 4 basic, primitive data types
        * What a variable is, why we need them, and how to use them
        * All of the different types of math and boolean operators,
            both comparative operators and arithmetic operators
        * Methods of using I/O
        * Formatting strings and their output
        * Using Escape Characters

    Functions used:
        * print() https://docs.python.org/3/library/functions.html#print
        * input() https://docs.python.org/3/library/functions.html#input
        * format() https://docs.python.org/3.5/library/string.html#format-string-syntax
        * ljust() https://docs.python.org/3/library/stdtypes.html#str.ljust
        * rjust() https://docs.python.org/3/library/stdtypes.html#str.rjust
        * center() https://docs.python.org/3/library/stdtypes.html#str.center
"""

# Variables
#  Ints
x = 5
y = 1
z = 9
#  Strings
myName = "John Doe"
myAddress = "123 Fake Street"
#  Booleans
myBool = True
#  Floats
a = 40.4
b = 164.6
c = 3.14159

print()
print("x:", x)
print("y:", y)
print("z:", z)
print()
print("myName:", myName)
print("myAddress:", myAddress)
print()
print("myBool:", myBool)
print()
print("a:", a)
print("b:", b)
print("c:", c)
print()

# Operators
#  Artithmetic Operators + - * / // % **
print("x + y:", x+y)
print("x + c:", x+c)
print("myName + \" \" + myAddress:", myName + " " + myAddress)
print("myName, myAddress:", myName, myAddress)
print("myBool + myBool")
print("c - b:", c-b)
print("x * y:", x*y)
print("c / a:", c/a)
print("z // x:", z//x)
print("a // c:", a//c)
print("z % x:", z%x)
print("z ** x:", z**x)
print()

#  Comparative Operators
print("z > x:", z>x)
print("z < x:", z<x)
print("z//x <= y:", z//x <= y)
print("y >= z:", y>=z)
print("z//x == y:", z//x == y)
print("a != b:", a != b)
print("z//x is y:", z//x is y)
print("not myBool:", not myBool)
print("True and False:", True and False)
print("True or False:", True or False)
print()

# Input and Output
myInput = input("Enter something: ")
print("myInput:", myInput)
print("{0} {1}".format(myInput, "asdf"))

print("myInput ljust: ", myInput.ljust(15, "_"))
print("myInput rjust: ", myInput.rjust(15, "_"))
print("myInput center: ", myInput.center(16, "_"))

# Escape Characters
print("This is \none print statement.")
print("I once read a quote and it said:\n\"Python is gr8 I sw8r\"")