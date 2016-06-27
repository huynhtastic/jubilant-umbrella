"""
	Author: Richard Huynh
	Date Created: 6/23/2016
	Assignment Code: 2-1
	Assignment Name: Bits of Ice Cream
	Description: Takes size of ice cream cone desired and outputs an
		ice cream cone made of bits. Only accepts odd values.

	#input #output #loops #control #errors #validation
"""

def solution():
	# takes input
	coneSize = int(input("Please enter your desired cone size!: "))

	# check if it's an odd number; exits program if odd
	if (coneSize % 2): # truthy; implicit true
		for i in range(0, coneSize, 2):
			output = ""
			for j in range(i + 1):
				output += str(j % 2) # makes 0 or 1 dependent on the remainder
			print(output)
	else: # false; even number inputted
		print("You didn't follow instructions! Good bye!")

solution()
