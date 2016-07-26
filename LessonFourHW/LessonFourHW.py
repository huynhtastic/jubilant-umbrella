"""
    Alexandra Triampol
    7/12/16
    This is a code for double transposition.
    It will decipher a text file called encrypted_logs.txt.
    There is an encrypt() method and decrypt() method.

"""

# allows code to read encrypted_logs.txt file
encryptedLogs = open('encrypted_logs.txt',"r")
textFile = encryptedLogs.readlines()
encryptedLogs.close()
encryptedMessages = []

for i in range(len(textFile)):
    encryptedMessages.append(textFile[i].rstrip('\n'))


# allows code to read decrypted_logs.txt file
decryptedLogs = open('decrypted_logs.txt',"r")
textFile = decryptedLogs.readlines()
decryptedLogs.close()
decryptedMessages = []

for i in range(len(textFile)):
    decryptedMessages.append(textFile[i].rstrip('\n'))


# fix the 4 when dividing the length of the string
def encrypt(encryptMessage):

    # creates the empty lists to hold the string values
    fireFList = []
    fireIList = []
    fireRList = []
    fireEList = []

    romeRList = []
    romeOList = []
    romeMList = []
    romeEList = []

    rangeNum = int(len(encryptMessage) / 4)

    start = 0
    afterStart = 1

    # put the string into the 4 different lists vertically
    # adds string to fireE,F,I,R lists

    if(len(encryptMessage)%4==0):
        for filling in range(0,rangeNum):
            fireFList.insert(filling,encryptMessage[start:afterStart])
            start += 1
            afterStart += 1
            fireIList.insert(filling,encryptMessage[start:afterStart])
            start += 1
            afterStart += 1
            fireRList.insert(filling,encryptMessage[start:afterStart])
            start += 1
            afterStart += 1
            fireEList.insert(filling,encryptMessage[start:afterStart])
            start += 1
            afterStart += 1

    if (len(encryptMessage) % 4 == 1):
        for filling in range(0, rangeNum):
            fireFList.insert(filling, encryptMessage[start:afterStart])
            start += 1
            afterStart += 1
            fireIList.insert(filling, encryptMessage[start:afterStart])
            start += 1
            afterStart += 1
            fireRList.insert(filling, encryptMessage[start:afterStart])
            start += 1
            afterStart += 1
            fireEList.insert(filling, encryptMessage[start:afterStart])
            start += 1
            afterStart += 1
        fireFList.append(encryptMessage[start:afterStart])

    if (len(encryptMessage) % 4 == 2):
        for filling in range(0, rangeNum):
            fireFList.insert(filling, encryptMessage[start:afterStart])
            start += 1
            afterStart += 1
            fireIList.insert(filling, encryptMessage[start:afterStart])
            start += 1
            afterStart += 1
            fireRList.insert(filling, encryptMessage[start:afterStart])
            start += 1
            afterStart += 1
            fireEList.insert(filling, encryptMessage[start:afterStart])
            start += 1
            afterStart += 1
        fireFList.append(encryptMessage[start:afterStart])
        start+=1
        afterStart+=1
        fireIList.append(encryptMessage[start:afterStart])

    if (len(encryptMessage) % 4 == 3):
        for filling in range(0, rangeNum):
            fireFList.insert(filling, encryptMessage[start:afterStart])
            start += 1
            afterStart += 1
            fireIList.insert(filling, encryptMessage[start:afterStart])
            start += 1
            afterStart += 1
            fireRList.insert(filling, encryptMessage[start:afterStart])
            start += 1
            afterStart += 1
            fireEList.insert(filling, encryptMessage[start:afterStart])
            start += 1
            afterStart += 1
        fireFList.append(encryptMessage[start:afterStart])
        start += 1
        afterStart += 1
        fireIList.append(encryptMessage[start:afterStart])
        start+=1
        afterStart+=1
        fireRList.append(encryptMessage[start:afterStart])

    # joins the characters from the FIRE lists into one string

    fireCharacters = ''.join(fireEList+fireFList+fireIList+fireRList)

    # adds the fireCharacters to the ROME lists to their appropriate spots
    count = 0
    plusCount = 1

    if(len(encryptMessage)%4==0):
        for fillingROME in range(0,rangeNum):
            romeRList.insert(fillingROME,fireCharacters[count:plusCount])
            count+=1
            plusCount+=1
            romeOList.insert(fillingROME, fireCharacters[count:plusCount])
            count += 1
            plusCount += 1
            romeMList.insert(fillingROME, fireCharacters[count:plusCount])
            count += 1
            plusCount += 1
            romeEList.insert(fillingROME, fireCharacters[count:plusCount])
            count += 1
            plusCount += 1

    if(len(encryptMessage)%4 ==1):
        for fillingROME in range(0, rangeNum):
            romeRList.insert(fillingROME, fireCharacters[count:plusCount])
            count += 1
            plusCount += 1
            romeOList.insert(fillingROME, fireCharacters[count:plusCount])
            count += 1
            plusCount += 1
            romeMList.insert(fillingROME, fireCharacters[count:plusCount])
            count += 1
            plusCount += 1
            romeEList.insert(fillingROME, fireCharacters[count:plusCount])
            count += 1
            plusCount += 1
        romeRList.append(fireCharacters[count:plusCount])

    if (len(encryptMessage) % 4 == 2):
        for fillingROME in range(0, rangeNum):
            romeRList.insert(fillingROME, fireCharacters[count:plusCount])
            count += 1
            plusCount += 1
            romeOList.insert(fillingROME, fireCharacters[count:plusCount])
            count += 1
            plusCount += 1
            romeMList.insert(fillingROME, fireCharacters[count:plusCount])
            count += 1
            plusCount += 1
            romeEList.insert(fillingROME, fireCharacters[count:plusCount])
            count += 1
            plusCount += 1
        romeRList.append(fireCharacters[count:plusCount])
        count += 1
        plusCount += 1
        romeOList.append(fireCharacters[count:plusCount])

    if (len(encryptMessage) % 4 == 3):
        for fillingROME in range(0, rangeNum):
            romeRList.insert(fillingROME, fireCharacters[count:plusCount])
            count += 1
            plusCount += 1
            romeOList.insert(fillingROME, fireCharacters[count:plusCount])
            count += 1
            plusCount += 1
            romeMList.insert(fillingROME, fireCharacters[count:plusCount])
            count += 1
            plusCount += 1
            romeEList.insert(fillingROME, fireCharacters[count:plusCount])
            count += 1
            plusCount += 1
        romeRList.append(fireCharacters[count:plusCount])
        count += 1
        plusCount += 1
        romeOList.append(fireCharacters[count:plusCount])
        count += 1
        plusCount += 1
        romeMList.append(fireCharacters[count:plusCount])

    # joins the characters from the ROME lists into one string
    romeCharacters = ''.join(romeEList+romeMList+romeOList+romeRList)

    print(romeCharacters)


# fix the 4 when dividing the length of the string
def decrypt(crypticMessage):
    romeRList = []
    romeOList = []
    romeMList = []
    romeEList = []

    fireFList = []
    fireIList = []
    fireRList = []
    fireEList = []

    tempRelocate = []
    finalRelocate = []

    rangeNum = int(len(crypticMessage) / 4)

    # Takes crypticMessage and puts it back into the ROME lists in the reverse order from encrypt()
    start = 0
    afterStart = 1

    if (len(crypticMessage) % 4 == 0):
        for romeE in range(0, rangeNum):
            romeEList.append(crypticMessage[start:afterStart])
            start += 1
            afterStart += 1
        for romeM in range(0, rangeNum):
            romeMList.append(crypticMessage[start:afterStart])
            start += 1
            afterStart += 1
        for romeO in range(0, rangeNum):
            romeOList.append(crypticMessage[start:afterStart])
            start += 1
            afterStart += 1
        for romeR in range(0, rangeNum):
            romeRList.append(crypticMessage[start:afterStart])
            start += 1
            afterStart += 1

    if (len(crypticMessage) % 4 == 1):
        for romeE in range(0, rangeNum):
            romeEList.append(crypticMessage[start:afterStart])
            start += 1
            afterStart += 1
        for romeM in range(0, rangeNum):
            romeMList.append(crypticMessage[start:afterStart])
            start += 1
            afterStart += 1
        for romeO in range(0, rangeNum):
            romeOList.append(crypticMessage[start:afterStart])
            start += 1
            afterStart += 1
        for romeR in range(0, rangeNum+1):
            romeRList.append(crypticMessage[start:afterStart])
            start += 1
            afterStart += 1

    if (len(crypticMessage) % 4 == 2):
        for romeE in range(0, rangeNum):
            romeEList.append(crypticMessage[start:afterStart])
            start += 1
            afterStart += 1
        for romeM in range(0, rangeNum):
            romeMList.append(crypticMessage[start:afterStart])
            start += 1
            afterStart += 1
        for romeO in range(0, rangeNum+1):
            romeOList.append(crypticMessage[start:afterStart])
            start += 1
            afterStart += 1
        for romeR in range(0, rangeNum+1):
            romeRList.append(crypticMessage[start:afterStart])
            start += 1
            afterStart += 1

    if (len(crypticMessage) % 4 == 3):
        for romeE in range(0, rangeNum):
            romeEList.append(crypticMessage[start:afterStart])
            start += 1
            afterStart += 1
        for romeM in range(0, rangeNum+1):
            romeMList.append(crypticMessage[start:afterStart])
            start += 1
            afterStart += 1
        for romeO in range(0, rangeNum+1):
            romeOList.append(crypticMessage[start:afterStart])
            start += 1
            afterStart += 1
        for romeR in range(0, rangeNum+1):
            romeRList.append(crypticMessage[start:afterStart])
            start += 1
            afterStart += 1

    # Takes the ROME lists and puts every character into 1 long list to temporarily hold them

    index = 0
    num = 0
    for relocating in range(0, rangeNum+1):
        try:
            tempRelocate.insert(index, romeRList[num])
            index += 1
        except IndexError:
            break
        try:
            tempRelocate.insert(index, romeOList[num])
            index += 1
        except IndexError:
            break
        try:
            tempRelocate.insert(index, romeMList[num])
            index += 1
        except IndexError:
            break
        try:
            tempRelocate.insert(index, romeEList[num])
            index += 1
            num += 1
        except IndexError:
            break

    # Converts the tempRelocate list into 1 long string
    romeCharacters = ''.join(tempRelocate)

    # Takes romeCharacters and puts it back into the FIRE lists in the reverse order from encrypt()
    begin = 0
    next = 1

    if (len(crypticMessage) % 4 == 0):
        for fireE in range(0, rangeNum):
            fireEList.insert(begin, romeCharacters[begin:next])
            begin += 1
            next += 1
        for fireF in range(0, rangeNum):
            fireFList.insert(begin, romeCharacters[begin:next])
            begin += 1
            next += 1
        for fireI in range(0, rangeNum):
            fireIList.insert(begin, romeCharacters[begin:next])
            begin += 1
            next += 1
        for fireR in range(0, rangeNum):
            fireRList.insert(begin, romeCharacters[begin:next])
            begin += 1
            next += 1

    if (len(crypticMessage) % 4 == 1):
        for fireE in range(0, rangeNum):
            try:
                fireEList.insert(begin, romeCharacters[begin:next])
                begin += 1
                next += 1
            except IndexError:
                break
        for fireF in range(0, rangeNum+1):
            try:
                fireFList.insert(begin, romeCharacters[begin:next])
                begin += 1
                next += 1
            except IndexError:
                break
        for fireI in range(0, rangeNum):
            try:
                fireIList.insert(begin, romeCharacters[begin:next])
                begin += 1
                next += 1
            except IndexError:
                break
        for fireR in range(0, rangeNum):
            try:
                fireRList.insert(begin, romeCharacters[begin:next])
                begin += 1
                next += 1
            except IndexError:
                break

    if (len(crypticMessage) % 4 == 2):
        for fireE in range(0, rangeNum):
            try:
                fireEList.insert(begin, romeCharacters[begin:next])
                begin += 1
                next += 1
            except IndexError:
                break
        for fireF in range(0, rangeNum + 1):
            try:
                fireFList.insert(begin, romeCharacters[begin:next])
                begin += 1
                next += 1
            except IndexError:
                break
        for fireI in range(0, rangeNum+1):
            try:
                fireIList.insert(begin, romeCharacters[begin:next])
                begin += 1
                next += 1
            except IndexError:
                break
        for fireR in range(0, rangeNum):
            try:
                fireRList.insert(begin, romeCharacters[begin:next])
                begin += 1
                next += 1
            except IndexError:
                break

    if (len(crypticMessage) % 4 == 3):
        for fireE in range(0, rangeNum):
            try:
                fireEList.insert(begin, romeCharacters[begin:next])
                begin += 1
                next += 1
            except IndexError:
                break
        for fireF in range(0, rangeNum + 1):
            try:
                fireFList.insert(begin, romeCharacters[begin:next])
                begin += 1
                next += 1
            except IndexError:
                break
        for fireI in range(0, rangeNum+1):
            try:
                fireIList.insert(begin, romeCharacters[begin:next])
                begin += 1
                next += 1
            except IndexError:
                break
        for fireR in range(0, rangeNum+1):
            try:
                fireRList.insert(begin, romeCharacters[begin:next])
                begin += 1
                next += 1
            except IndexError:
                break

    # Takes the FIRE lists and puts every character into 1 long list to temporarily hold them
    num = 0
    reorderingIndex = 0

    for reordering in range(0, rangeNum+1):
        try:
            finalRelocate.insert(reorderingIndex, fireFList[num])
            reorderingIndex+=1
        except IndexError:
            break
        try:
            finalRelocate.insert(reorderingIndex, fireIList[num])
            reorderingIndex += 1
        except IndexError:
            break
        try:
            finalRelocate.insert(reorderingIndex, fireRList[num])
            reorderingIndex+=1
        except IndexError:
            break
        try:
            finalRelocate.insert(reorderingIndex, fireEList[num])
            reorderingIndex+=1
        except IndexError:
            break
        num+=1

    # Converts the finalRelocate list into 1 long string
    fireCharacters = ''.join(finalRelocate)

    print(fireCharacters)


# to loop through the list (contains info from the text files)

for index in range(0,len(encryptedMessages)):
    decrypt(encryptedMessages[index])

for index in range(0,len(decryptedMessages)):
    encrypt(decryptedMessages[index])