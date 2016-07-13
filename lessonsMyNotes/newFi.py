print(list(range(0, 10, 1)))

aList = [1, 2, 3]
print(aList)

#boolean operator
print(1 in aList) #true
print('A' in aList)

for i in range(0, 10):
    print(i)

    #advanced for loop
for item in aList:
    print(item)

    #while loops
x = 3
while (x>0):
    print (x)
    x-=1

    """
    if statements
    if ('expression ' == True):

        """
    print()
    x = 'asdf'
    if (x == 2):
        print(x)
    elif (x == 3):
        print(x)
    else:
        print(x, "isn't a number maybe")


    #for else
        print( )
        while (x > 0):
            print (x)
            x-=1
        else:
            print("x i equal to 0")

        #break continue
        for i in range(0, 10):
            if (i == 5):
                print ("im broke")
               # break
            elif (i == 6):
                print('gonna do ')
                continue
            else:
                print(i)
            print("finished chekcing if cond")
        else:
            print('some else')

#pass

for i in range(0, 10):
    if (i < 5):
        print(i)
    elif(i == 7):
        pass #tells frogram to do nothing, can't leave it blank so just write pass if you really need else
    else:
        print(i, "some things")


#nested loops
a = ["apple", "banana", "kiwi"]
for fruit in a:
    for letter in fruit:
        print(letter)