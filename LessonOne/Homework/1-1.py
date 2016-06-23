"""
	Author: Richard Huynh
	Date Created: 6/21/2016
	Assignment Code: 1-1
	Assignment Name: Dr. J. Dan's Guest Greeter
	Description: Takes name, age, and favorite ice cream flavor as 
		input and outputs them in a formatted string. 

	#input #output #string #format #concatentation
"""

def solution():
	# grab inputs
	name = input("Please enter your full name: ")
	age = int(input("Please enter your age: "))
	flavor = input("Please input your favorite ice cream flavor: ")

	# print output
	print("\nWelcome, {0}! Congratulations on being on this planet for the past {1} years! Have as much {2} ice cream as you want at the party!\n".format(name, age, flavor))

solution()
