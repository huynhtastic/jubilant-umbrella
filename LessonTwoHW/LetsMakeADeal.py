"""
    Alexandra Triampol
    6/24/16
    This is a code that shows a game called "Let's Make a Deal".
    The code will generate all the numbers: The prize door number,
    the initial door guess, the door shown, and the final guess.
    If you win, it will add to your winning streak.  User input will
    allow you to see how each round went.

    *Still needs work...*
"""

"""
    ---prompt user for how many rounds (user input)
    times won (variable)
    number [1,3] = prize (random variable)
    number [1,3] = guess (variable)
    number != prize or guess = shown (variable)
    new guess (variable)
    compare new guess if = prize
    if correct +1 to times won
    get probability for switching answers
    get probability for not switching answers

"""

from random import randint

# initialize everything
roundsWon = 0
prizeNum = randint(1, 3)
initialGuess = randint(1, 3)
doorShown = randint(1,3)
finalGuess = randint(1, 3)

#asks how many rounds to "play"
rounds = int(input("How many rounds do you wish to play? "))

#prints out the new generated numbers
def newGuess():
    finalGuess = randint(1, 3)
    doorShown = randint(1, 3)
    roundsWon = 0
    while(doorShown == initialGuess or prizeNum):
        doorShown = randint(1,3)
        if(doorShown != initialGuess or prizeNum):
            break
    while(finalGuess == initialGuess or doorShown):
        finalGuess = randint(1,3)
        if (finalGuess == prizeNum):
            roundsWon+=1
            break

switchWinProb = roundsWon/rounds
noSwitchWinProb = 1-switchWinProb

#prints out the results from the rounds
def printEndResults():
    print("Prize Door "," Initial Guess "," Door Shown "," Final Guess ")
    print("\t",prizeNum,"\t","\t","\t",initialGuess,"\t","\t","\t","\t",doorShown,"\t","\t","\t",finalGuess)
    print("Winning Streak:",roundsWon)
    print("Winning Probability:",switchWinProb)
    print("Didn't Switch Guess Winning Probability:", noSwitchWinProb)


# start the process of initializing the functions
#repeating rounds
for i in range(0,rounds):
    newGuess()
    prizeNum = randint(1, 3)
    initialGuess = randint(1, 3)
    doorShown = randint(1,3)
    finalGuess = randint(1, 3)
    doorShown = randint(1,3)
    newGuess()
    printEndResults()