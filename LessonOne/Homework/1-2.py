"""
	Author: Richard Huynh
	Date Created: 6/21/2016
	Assignment Code: 1-2
	Assignment Name: The root(s) of all evil
	Description: Takes a, b, c and calculates the roots with given 
		inputs. Allows errors to be thrown.

	#input #output #operators #math 
"""

# from math import sqrt

def solution():
	# grab inputs
	a = int(input("Please enter a valid 'a': "))
	b = int(input("Please enter a valid 'b': "))
	c = int(input("Please enter a valid 'c': "))

	# calculate the thing
	# ax^2 + bx + c
	# x = (-b) +- sqrt(b^2 - 4ac) / 2a
	posX = ((-b) + (((b**2) - (4 * a * c)) ** .5)) / (2 * a)
	negX = ((-b) - (((b**2) - (4 * a * c)) ** .5)) / (2 * a)
	print (posX, negX)

solution()