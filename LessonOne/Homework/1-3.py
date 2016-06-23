"""
	Author: Richard Huynh
	Date Created: 6/21/2016
	Assignment Code: 1-3
	Assignment Name: Tell me the TRUTH
	Description: Outputs the solutions for the note left at the scene
		of the crime.

	#boolean #logic #truthtables #evaluation #evaluation operators
"""


def solution():
	print()

	input("(TRUE and TRUE): At 5:00PM, I woke up from my cot at the corner of 28th and Freeo.")
	print(True and True, "\n")

	input("(FALSE and TRUE): At 6:00PM, I zipped down to the docks and slipped on a banana.")
	print(False and True, "\n")

	input("(TRUE or FALSE): At 7:00PM, I walked past the Spintel Hospital and saw a cute dog.")
	print(True or False, "\n")

	input("((TRUE or FALSE) and FALSE): At 8:00PM, I followed the dog back to its owner, but oh man it has an owner.")
	print ((True or False) and False, "\n")

	input("((TRUE or FALSE) or (FALSE and FALSE)): At 10:00PM, I see the dog coming out for a potty break. Is it time to make the snatch?")
	print((True or False) or (False and False), "\n")

	input("((TRUE and TRUE) and (FALSE or FALSE or TRUE)): At 11:00PM, I have the dog. I'm making a break for it!")
	print((True and True) and (False or False or True), "\n")

	input("((FALSE and TRUE) or (TRUE and FALSE) and (TRUE and TRUE)): At 12:00AM, I forgot my keys at the house. I gotta go back.")
	print((False and True) or (True and False) and (True and True), "\n")

	input("((TRUE or FALSE and TRUE) and (TRUE or FALSE and TRUE)): At 1:00AM, I took the dog out for a walk at Intelee Park. HE'S SO CUTE!")
	print((True or False and True) and (True or False and True), "\n")

	input("(TRUE and TRUE and FALSE or TRUE and FALSE or TRUE): At 2:00AM, I decided to name the dog Genie. He's definitely a husky. Freakin' cute I swear.")
	print(True and True and False or True and False or True, "\n")

	input("(((TRUE and FALSE or TRUE) and (FALSE or TRUE) or (FALSE and FALSE)) and TRUE): At 3:00AM, I forgot to leave a cool riddle at the scene of the crime. I'm going back.")
	print(((True and False or True) and (False or True) or (False and False) and True), "\n")

	input("((TRUE and TRUE) or (TRUE and FALSE) or (TRUE and FALSE) and (TRUE and TRUE)): At 4:00AM, I remembered that I had already left the riddle. I'm the best.")
	print((True and True) or (True and False) or (True and False) and (True and True), "\n")

	input("((FALSE or TRUE) or (FALSE or TRUE) or (TRUE or FALSE) or (TRUE or FALSE) or (TRUE or FALSE) or (TRUE or FALSE)): At 5:00AM, I'm gonna go have breakfast at a dog friendly place. Probably like P. Husky's.")
	print((False or True) or (False or True) or (True or False) or (True or False) or (True or False) or (True or False), "\n")

solution()
