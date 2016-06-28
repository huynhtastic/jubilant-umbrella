"""
Alexandra Triampol
6/21/16
This code allows the user to solve quadratic equations.
This requires 3 integers from the leading coefficients
of the polynomials in the quadratic equation.
(If the numbers weren't "nice integers", an error will occur.
"""

# import the math functions to do the square root function
from math import *

# take in all the user inputs (typed in integers)
a = input("Give me the leading coefficient of the first polynomial: ")
b = input("Give me the leading coefficient of the second polynomial: ")
c = input("And now the last leading coefficient for the third polynomial: ")

# converts the user input from a string to an integer for the actual solving
aInt = int(a)
bInt = int(b)
cInt = int(c)

# computes the quadratic formula twice, once for subtracting "b" and again for adding "b"
answerSubtract = ((-bInt - (sqrt(bInt**2 - 4*aInt*cInt)))//2*aInt)
answerAdd = ((-bInt + (sqrt(bInt**2 - 4*aInt*cInt)))//2*aInt)

# prints out the two numbers
print(answerSubtract , answerAdd)