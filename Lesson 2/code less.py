"""
Control structures
there are Ranges and LIst
Ranges are a key word and data structure
costum python made class that generates a type o list
range(x,y,step)
x= starting number
y= number of stops at (-1)
steps: number to increments by

Lists are arrays
[a,b,c]
they can be ints, string, floats, boolean, classes, functions, lambda ect.

"""

print(list(range(0,10,1)))

aList= [1,2,3]
print(aList)

"""
in operator
this is used as a booleans or fro somethign to pull from a list(or like a list)

"""
#boolean
print(1 in aList)
#this will return True b/c there 1 is in the aList

print('A' in aList)
#this will return False b/c this is not in aList

"""
    for loop will run though a range of numbers, items of a list, or other daa structer
    for i in range(0, 10, 1) = for i in range(1, 10)
    each tun though in a loop is called an iteration
"""

for i in range(0,10):
    print(i)

for item in aList:
    print(item)
"""
while loop allows you to loop though while an expresion inside evaluates to true
ex.
while('expression' == True):

"""
x=3
while (x>0):
    print(x)
    x-=1
#this is used when you dont know what your limit is