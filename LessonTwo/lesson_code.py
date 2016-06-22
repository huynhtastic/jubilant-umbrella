"""
    Control Structures

    Ranges & Lists

    Ranges
    range(x, y, step)
     - x: starting
     - y: number to stop at (-1)
     - step: the number to increment by

    List: arrays
    [a, b, c]
    ints, string, floats, booleans, classes, functions, lambda
    [[]]
"""

print(list(range(0, 10, 1)))

aList = [1,2,3]
print(aList)
# print(bList)

"""
    in operator
    boolean operator or pull from list
"""

# boolean operator
print (1 in aList) #true
print ('A' in aList) #false

"""
    for
    loop through a range of number, items of a list
    for i in range(0, 10, 1) = for i in range(0, 10)
"""
print()
for i in range(0, 10):
    print (i)
    """ extra code """
else:
    # if you reach the end of the list
    print ("you have reached the end of the list")

print()

for item in aList:
    print (item)

"""
    while ('expression' == True):
    while loops while expression is true
"""
x = 3
print()
while (x > 0):
    print (x)
    x -= 1
else:
    # runs when the expression in the while loop is false
    print ("x is equal to 0\n")

for x in range(3, 0, -1):
    print (x)

"""
    if statements
    if ('expression' == True):
        'code'
    elif ('expression' == True):
        'elif code'
    else:
        'else code'
"""
print()
x = 'asdf'
if (x == 2):
    print(x)
elif (x == 3):
    print(x)
elif (x == 4):
    print(x)
# else:
#     print(x, "isn't a number maybe")

"""
    break continue
    break - if the interpreter ever reaches break, break out of the preceding loop

    continue - stops the iteration and goes to the next iteration

"""
print()
for i in range(0, 10):
    if (i == 5):
        print ("i'm breaking")
        # break
    elif (i == 6):
        print("gonna jsut continue")
        continue
    else:
        print(i)

    print("finished checking if conditions")
else:
    print("some else code")

"""
    pass - do nothing
"""

for i in range(0, 10):
    if (i < 5):
        print (i)
    elif (i == 7):
        pass
    else:
        print(i, "some things")

"""
    nested loops
"""
a = ["apple", "banana", "kiwi"]
# "apple" = ["a", "p", "p", "l", "e"]
for fruit in a:
    for letter in fruit:
        print(letter)

