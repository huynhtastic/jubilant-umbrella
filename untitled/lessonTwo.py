"""
    Author: Cynthia Zaragoza
    Date Created: 6/24/2016
    Assignment Name: The Odd One
    Desription: Cones made up of 1's and 0's with the biggest input as the width of the cone.
    ex: width of 5
                        01010
                         010
                          0
"""
#make the width the first line
yourCone = int(input("What width do you want your cone?"))

#super pseudo code divide yourCone by two then make that the number of lines printed
#make loop so that it will go from 0 to yourCone and alternate b/w 1 & 0
#center the output a certain number of spaces from the left (by maybe just adding one space for each line, by keeping track of the lines)
print()
x = yourCone

while(x > 1): #this is for the first line
    if (x%2 == 0):#if the first number is even then print 0
        print(1)
    else:
        print(0)
    yourCone-2



#have the other lines centered while keeping them in the center, find phonon mark that starts the cone yourCone -2away from the left
        #if yourCone is
            #center(yourCone- i):

