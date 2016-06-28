"""
	Author: Rachel Schreiber
	Date Created: 6/24/2016
	Assignment Code: 2-2
	Assignment Name: Let's Make a Deal
	Description:
	    Create a simulation for Monty Hall problem, showing probability of winning if person switches doors
"""

# google python random module to learn more about this module!
import random
random.seed()
def solution():
    win = 0
    rounds = int(input("Enter number of times you want to play: "))
    print("Prize".center(10, ' ') + "Guess".center(10, ' ') + "View".center(10, ' ') + "New Guess".center(10, ' '))
    for i in range(0, rounds):
        prize = random.randint(1,3)
        guess = random.randint(1,3)
        view = random.randint(1,3)
        while(view == prize or view == guess):
            view = random.randint(1,3)
        if (guess + view == 3): # guess = 1 and view = 2 or guess = 2 and view = 1
            newGuess = 3
        elif (guess + view == 4):   # guess = 1 and view = 3 or vice versa
            newGuess = 2
        else:       # guess = 2 and view = 3 or vice versa
            newGuess = 1
        if(newGuess == prize):
            win += 1
        print(str(prize).center(10, ' ') + str(guess).center(10, ' ') + str(view).center(10, ' ') + str(newGuess).center(10, ' '))
    print("Probability of winning if you switch: " + str(win/rounds))
    print("Probability of winning if you do not switch: " + str(1-win/rounds))

solution()