"""
    Author: Rachel Schreiber
	Assignment Code: 1-2
	Assignment Name: The root(s) of all evil
	Description:
        Find roots of quadratic equation
"""
print("Welcome to the quadratic formula roots finder!")
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))
temp = (b**2 - 4*a*c) ** (1/2)
x1 = (-b + temp)/(2*a)
x2 = (-b - temp)/(2*a)
print("The two roots are: {0} and {1}".format(x1, x2))
