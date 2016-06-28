"""
    Author: Rachel Schreiber
    Date Created: 6/24/2016
	Assignment Code: 2-1
	Assignment Name: The Odd One
	Description:
        Specify width of cone, and alternate 0's and 1's
        Each row of cone starts with 0
        ex: width of 5
            01010
             010
              0
"""
width = int(input("What's the width? "))
row = ""
if(width%2 == 0):
    print("Sorry, we need an odd number for the width.")
else:
    for i in range(width//2, -1, -1):
        for j in range(0, i):
            row += "01"
        row += "0"
        print(row.center(width, ' '))
        row = ""