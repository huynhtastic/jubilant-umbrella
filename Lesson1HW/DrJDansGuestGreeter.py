"""
Alexandra Triampol
6/21/16
This code creates a greeting that uses user input
such as their full name, age, and favorite ice cream.
"""

# takes in user input for the greeting

fullName = input("What is your first and last name?: ")
age = input("How old are you? (if you don't mind me asking): ")
iceCream = input("What kind of ice cream do you like?: ")

# prints out the greeting

print("") # aesthetic spacing
print("Welcome,",fullName + "!")
print("Congratulations on surviving for",age,"years!")
print("You deserve all the", iceCream, "ice cream in the world!")

# use .format{fullName,age,iceCream}