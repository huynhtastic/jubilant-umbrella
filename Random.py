import random

plays= int(input("Enter number of times you want to play: "))

winssw=0

for i in range(0,plays):
    prize=(random.randrange(1, 4))
    guess=(random.randrange(1,4))
    view=(random.randrange(1,4))
    while(view==prize or view==guess):
        view=(random.randrange(1,4))
    if(guess==2 and view==3 or guess==3 and view==2):
        newguess=1
    elif(guess==1 and view==3 or guess==3 and view==1):
        newguess=2
    else:
        newguess=3
    if(newguess==prize):
        winssw=winssw+1
    print(prize,guess,view,newguess)

probwin=winssw/plays
noswitch=1-probwin
print("Prob of winning by switching is " + str(probwin)+ "." )
print("Prob of winning by not switching is "+str(noswitch)+ ".")



