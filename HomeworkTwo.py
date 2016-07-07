width = int(input("Please enter the largest width of the cone: "))

nw1 = int(width/2+1)
nw2 = int(width/2+1)

x = 1
for i in range(0, nw1):
    one = ""
    zero ="0"
    for j in range(1, x):
        one = one + " "
    for k in range(1, nw2):
        zero= zero+"1"+"0"
    x = x+1
    nw2 = nw2-1
    print(one+zero)

"""
if (width % 2 == 0):
    y = int(zero[0:3])
    #x = int(str(one + zero)[:-2])
    print(one, y)
        # print(one+(zero.length-2))
else:
    print(one + zero)
"""

import random

number = int(input("How many times would you like to play? "))
swins = 0
print("Prize","\t","Guess","\t","View","\t","New Guess")

for i in range(0, number):
    prize = random.randint(1, 3)
    guess = random.randint(1, 3)
    for j in range(1, 4):
        if(prize!= j and guess!= j):
            view = j
    for k in range(1, 4):
        if(view!= k and guess!= k):
            newGuess= k
    if(prize == newGuess):
        swins = swins+1
    print(" ",prize,"\t"," ",guess,"\t"," ",view,"\t","  ",newGuess)

wbswitch = swins/number
wbnswitch = 1- wbswitch
print("Probability of winning if you switch = " + str(wbswitch))
print("Probability of winning if you dont't switch = " +str(wbnswitch))
