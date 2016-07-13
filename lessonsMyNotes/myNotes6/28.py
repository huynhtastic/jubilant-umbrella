"""
    Python data structures

    Lists   denoted with square brackets
    -array that holds stuff
        -anything (list, chars, strings, functions, classes)
    -mutable: once it's instanciated, its easily overwritten
    -nonhomogenous: can have anything in list
        -i.e. ['a string', 5, [1, 3, 2, 4]]
    -length- independent
        -[1, 2, 4]   can easily make it length of 4
    -can do anything, most flexable out of all python data types, can hold anything
"""
aList = [2, 4, 5]
print('alist', aList)

#add to list, key word for lists is append: function that you call for a list
aList.append(4)
print('aList append', aList)
aList. append('5')
print('aList append', aList)

#remove
aList.remove(2)
print('aList remove', aList)

#indexing a list [ ]
firstElement = aList[0]
print('remove firstElement of aList', firstElement)

#pop removeing from list but also storing it somewhere
poppedElement = aList.pop()
print('poppedElement:', poppedElement)

#can also pop specific index
poppedElement = aList.pop(2)
print('popppedElement at index 2:', poppedElement)

"""
    Indexing and Slicing
    Index - its place in the array
"""
print()
bList = ('my', 'name', 'is', 'john', 'doe')

#print([:3]) #ends at 3 but it doesn't take 3

"""
Sets
    useful when making a list of duplicates and don't want duplicates
"""
duplicates = [1, 1, 2, 2, 3, 3]
aSet = set(duplicates) #comes out w/ {} but never actually type it
print(aSet)
aSet.add(4)
print(aSet)
aSet.remove(1)
print(aSet)

"""
Dictionaries/Hashes/Maps/HashMap second most used data structure
    denoted with {}
    denoted as containers with key value pairs: If you want to access  specific element in dictionary you have to know its key
            -don't use indices
            -USE keys
                -can be strings or integers
                -once a key is inside can't change what it is, ues a lot of memory
            -values
                -can be anything: other dict., tuple, set, int, char
    -usefull data structure, easy, powerfull, fast
    -print in random order, but can make them ordered
"""
aDict = {#empty dictionary
    'a': 'apple',        #key:value
    'b':'banana',
    'c': 'cherry'

}
print(aDict['a'])
print(aDict['b'])

#add to dictionary
aDict['d'] = 'dragonfruit' #access, instractuate it
print(aDict['d'])

#see all keys
print(aDict.keys())#function that returns list of keys, basically a list

#see all values
print(aDict.values())

#all keys and values
print(aDict.items())

"""
    Performance, Time complexity, Expense

    PERFORMANCE
    - IF SOMething runs fast

    Time Complxity
    - how long something will take to run or perform an operation
    - Big (O) notation
    - O (1) - no matter how much data you have, performance is constant
                ex. [1,2,3,4] .001 u-seconds to pop 4
    - O (n) - your time scles linerarly with your data size, better for larger numbers
                ex.[1, 2, 3, 4, 5] 1 second to print each value
                in the list
                [1, 2, 3, 4, 5, ] 2 sec. to print each value
                -O(2n+2)
    - O (n^2) - time scales exponentially with you data
    ex. [1, 2, 3, 4, 5] 3 seconds to bubble sort
    - O (log(n)) - choice delineation
        ex. bunch of branches
    - n is the number of items/elements

    Expense
    - "Is it expenseive to do x?"
"""

"""
    Error Handling fun stuff
    Exception handling
    Error Catching

-anything that causes program to break
        -can't run
        -problems with code
        - anything that causes prog. to break

    three types of errors
    -Compile-time errors
    -Runtimes errors
    -Logic errors

    Try Ecept
    Raise Finally

    Try -- try to do something that might result in a run time eror
        error
    Except -- un this code if the try results in a n error
    Finally -- code that is run nomater what
    Raise -- ceate an error and end to user
"""
print()
try:
    print(aVariable)
    myVar = int('a')
    myVar = 5/0
except (ValueError, ZeroDivisionError):
    print('you ran into a Value or ZeroDivision error')
except NameError: #referencing a variable before instantation
    print('You ran into a Name Error')
finally:
    print("you're done")

try:
    raise Exception('eggs')
except Exception as exc:
        print(exc)