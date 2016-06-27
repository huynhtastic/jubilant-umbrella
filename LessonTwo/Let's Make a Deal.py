from random import randint
play = int(input("How many time do you want to play?"))
wins = 0
print("Prize","\t","Guess","\t","View","\t","New Guess")
for x in range(0,play,1):
    prize = randint(1,3)
    guess = randint(1,3)
    for y in range(1,4,1):
        if(prize!=y and guess!=y):
            view = y
    for z in range(1,4,1):
        if(view!=z and guess!=z):
            newGuess=z
    if(prize==newGuess):
        wins = wins+1
    print(" ",prize,"\t"," ",guess,"\t"," ",view,"\t","  ",newGuess)
probability = wins/play
print("Probability of winning if you switch: "+str(probability))





