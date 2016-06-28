"""
    Author: Rachel Schreiber
	Assignment Code: 1-1
	Assignment Name: Dr. J. Dan's Guest Greeter
	Description:
        Ask for name, age, and favorite flavor of icecream, then greet person
"""
name = input("Please enter your first and last name (ex: John Smith): ")
age = input("How old are you? ")
flavor = input("One last question, and you're free to go! What's your favorite icecream flavor? ")
print("Welcome, {0}! Congratulations on being on this planet for the past {1} years! Have as much {2} icecream as you want at the party!".format(name, age, flavor))