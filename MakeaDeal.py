from random import randint
def deal():
    times = int(input("How many times do you want to play?    "))
    switchwins = 0
    print("Prize\tGuess\tView\tNew Guess")
    for x in range(0, times):
        realdoor = randint(1, 3)
        guess = randint(1, 3)
        if ((realdoor != 1) and (guess != 1)):
            view = 1
        elif ((realdoor != 2) and (guess != 2)):
            view = 2
        elif ((realdoor != 3) and (guess != 3)):
            view = 3
        if ((guess != 1) and (view != 1)):
            newguess = 1
        elif ((guess != 2) and (view != 2)):
            newguess = 2
        elif ((guess != 3) and (view != 3)):
            newguess = 3
        print("\t", realdoor, "\t\t", guess, "\t\t", view, "\t\t", newguess)

        if newguess == realdoor:
            switchwins += 1
    print("Probability of winning if you switch =", round((switchwins/times), 2))
    print("Probability of winning if you stay =", round((1-(switchwins/times)), 2))

deal()