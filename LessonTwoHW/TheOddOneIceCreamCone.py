"""
	Alexandra Triampol
	6/24/2016
	This code makes an ice cream cone out of one's and zero's
	based on user input for the width of the cone.
	Ex: Size - 5        0 1 0 1 0
	                      0 1 0
	                        0
	*Still needs work...*
"""

zero = 0
one = 1
coneSize = int(input("Size: "))


"""
for i in range(coneSize + 1):
    num = coneSize - i
    print (' ' *num + '0 ' +'1 ' * i)
"""


for i in range(coneSize,0,-2):
    for j in range(0,coneSize):
        print(zero,one,end=" ")
    print()


"""
for i in range(coneSize,0,-1):
    #print(zero,one, end=" ") ---> 0 1 0 1 0 1 0 1 0 1
    for j in range(0,coneSize):
        print(zero,end="")
    for j in range(0,coneSize):
        print(one, end="")
    print()

"""