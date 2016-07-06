"""
    Python's built in data structures

    Lists []
    - Array that holds stuff
        - Anything
        ex. lists, strings, functions, lambdas, classes, etc.
    - mutable
    ex. [1,2,3] -> [2,2,3]
    - non-homegenous
    ex. ['a string', 5, [1,2,3]]
    - length-independent
    [1,2,3] (length=3) -> [1,2,3,4] (length=4)
    - iterable - can access elements within this thing

    index - its place in the array
    ex. ['a', 'string', 'asdf']
        [ 0,      1,       2  ]

    mutable & immutable
    mutable - changable or can be edited or overwritten
    immutable - not changeable or edited or overwritten

    homogenous - same; only allows the same data type
    ex. [only integers], [only strings]
"""
aList = [1,2,3]
print('alist', aList)

# adding a list: append
aList.append(4)
print('alist append', aList)
aList.append('5')
print('append "5"', aList)

# removing from a list: remove
aList.remove(1)
print('alist remove', aList)
# aList.remove(1)
# print('remove 1', aList)

# indexing a list []
firstElement = aList[0]
print('firstElement of aList', firstElement)

# pop from list: pop
poppedElement = aList.pop()
print('poppedElement:', poppedElement)
print('aList:', aList)
poppedElement = aList.pop(1)
print('poppedElement:', poppedElement)

"""
    Indexing and Slicing
    index - its place in the array
    ex. ['a', 'string', 'asdf']
        [ 0,      1,       2  ]
    indexing/accessing/retrieving - accessing the element at the desired index

    Slicing - advanced indexing; indexes multiple elements at the same time
    [:]
"""
print()
bList = ['my', 'name', 'is', 'john', 'doe']
print(bList[1])
print(bList[2], bList[4])
# slicing
print(bList[0:4])
print(bList[:3]) # bList[0:3]

# indexing backwards
print(bList[4])
print(bList[-1])
print(bList[-1:1])
print(bList[-1:1:-1])

print(bList[1:5])
print(bList[1:])
print(bList[::2]) # changing step

# back to strings
print()
aString = 'abcdefg'
print(aString[2])
print(aString[:6])
print(aString[-1])

# modifying a list element
print()
print('bList', bList)
bList[-2] = 'richard'
print('bList with Richard', bList)
bList[0:3] = 'asdf' # 'asdf' = ['a', 's', 'd', 'f'] replace and then add extras
print('bList with asdf', bList)
# print(bList[7]) throws index out of range

"""
    Tuples ()
    - just like a list
        - non-homogenous
        - iterable
    - UNLIKE A LIST
        - immutable
        - length-dependent
"""
print()
aTuple = (1,2,3,4,5)
print('aTuple', aTuple)
# aTuple.add(6)
# print('added 6', aTuple)
print(aTuple[0])
bTuple = (6,7,8)
cTuple = aTuple + bTuple
print(cTuple)

"""
    Sets {}
    - like a list
        - holds things
        - iterable
        - length-independent
    BUT...
        - homegenous
        - immutable
        - only contain unique values
"""
duplicates = [1,1,2,2,3,3]
aSet = set(duplicates)  #set()
print(aSet)
aSet.add(4)
print(aSet)
aSet.remove(1)
print(aSet)

# unions, intersections, differences, symmetric_differences

"""
    Dictionaries/Hashes/Maps/HashMap {}
    - containers with key: value pairs
        - don't use indices
        - instead, they use keys
    - keys
        - can be strings, integers
        - immutable
    - values
        - literally can be anything
    - unordered
"""
print()
aDict = {#empty dictionary {}
    'a': 'apple',
    'b': 'banana',
    'c': 'cherry'
}
print(aDict['a'])
print(aDict['b'])
# adding
aDict['d'] = 'dragonfruit'
print(aDict['d'])

# see all keys
print(aDict.keys())

# values
print(aDict.values())

# see all keys & values
print(aDict.items())

"""
    Performance, Time complexity, Expense

    Performance
    - if something fast

    Time complexity
    - how long something will take to run or
        perform an operation
    - Big(O) notation
        - O(1)- no matter how much data you have,
            time performance is constant; most optimal
            ex. [1,2,3,4,5] .001 u-seconds to pop 5
                [1,2,3] .001 u-seconds to pop 3
        - O(n) - your time scales linearly with your data size
            ex. [1,2,3,4,5] 1 second to print each value
                in the list
                [1,2,3,4,5,6,7,8,9,10] 2 seconds to
                print each value
            - O(2n+2) = O(n)
        - O(n^2) - time scales exponentially with your data
            ex. [1,4,3,2,5] 3 seconds to bubble sort
        - O(log(n)) - choice delineation; better for larger numbers
            ex. bunch of branches( if statements )
                n is number of branches
        - n is the number of items/elements in the dataset

    Expense
    - "Is it expensive to do x?"
        - Well, is it fast? What time complexity
            does it run under?
        - How much memory does it take?

"""

"""
    Error Handling
    Exception Handling
    Error Catching

    Error - when your code can't compile
        - can't run
        - any problem with code
        - anything that causes your program to break

    Three types of errors
    - Complile-time
    - Runtime
    - Logic errors

    Try Except
    Raise Finally

    Try -- try do something that might result in a runtime
        error
    Except -- run this code if the try results in an error
    Finally -- code that is run no matter
    Raise -- create an error and send to user
"""
print()
# myVar = int('a')
try:
    print(aVariable)
    myVar = int('a')
    myVar = 5/0
except (ValueError, ZeroDivisionError):
    print('You ran into a Value or ZeroDivision Error')
except NameError as a: # referencing a variable before instantiation
    # print('You ran into a Name Error')
    print("Error:", a)
finally:
    print("You're done catching errors!")

try:
    raise Exception('you didn\'t crack the eggs')
except Exception as exc:
    print(exc)

# raise(Exception('you didn\'t make eggs'))

num = int(input("Please enter a number under 100: "))
if (num >= 100):
    raise(Exception('u didnt listen 2 me'))