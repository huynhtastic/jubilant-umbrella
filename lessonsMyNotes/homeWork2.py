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
yourCone = int(input("What width do you want your cone?"))

#super pseudo code divide yourCone by two then make that the number of lines printed
#make loop so that it will go from 0 to yourCone and alternate b/w 1 & 0
#center the output a certain number of spaces from the left (by maybe just adding one space for each line, by keeping track of the lines)

length = yourCone
x = length
print()
while x >= 1:
    answer = " "
    i = 0
    for i in range(x):
        if (i % 2 == 0): #if the first number is even then print 0
            answer += '0'
        else:
            answer += '1'
    print(answer.center(yourCone, " "))
    x -=2
