""""
Author: Cynthia Zaragoza
    Date Created: 7/7/2016
    Assignment Name: The Key to Success
    Description: Create two methods: one that deciphers
                text and one that ciphers any text given to it
"""
#input to be ciphered
ciph = ''

#input to be deciphered
dc = 'djkky'

#depending on what needs to be ciphered or
    #deciphered will depend on if the string
    #empty or not
if len(ciph) >= 1:
    # make dictionary do encipher word
    toCiph = {'a': 'c',
         'b': 'w',
         'c': 'm',
         'd': 'f',
         'e': 'j',
         'f': 'o',
         'g': 'r',
         'h': 'd',
         'i': 'b',
         'j': 'a',
         'k': 'n',
         'l': 'k',
         'm': 'g',
         'n': 'l',
         'o': 'y',
         'p': 'p',
         'q': 'h',
         'r': 's',
         's': 'v',
         't': 'e',
         'u': 'x',
         'v': 't',
         'w': 'q',
         'x': 'u',
         'y': 'i',
         'z': 'z'
         }

    # create empty string to add new letters and print
    realW = ''

    #make for loop that goes through
    for element in ciph:
        for letter in element:
            realW += toCiph[letter] #add letter to be outputed
        # print(toCiph[letter])
    print(realW)

else:
    ciphDict = {
    'c': 'a',
    'w': 'b',
    'm': 'c',
    'f': 'd',
    'j': 'e',
    'o': 'f',
    'r': 'g',
    'd': 'h',
    'b': 'i',
    'a': 'j',
    'n': 'k',
    'k': 'l',
    'g': 'm',
    'l': 'n',
    'y': 'o',
    'p': 'p',
    'h': 'q',
    's': 'r',
    'v': 's',
    'e': 't',
    'x': 'u',
    't': 'v',
    'q': 'w',
    'u': 'x',
    'i': 'y',
    'z': 'z'
}
    #create empty string
    otherWord = ''
    for element in dc:
        for letter in element:
            #add corresponding characters to string
            otherWord += ciphDict[letter]
    print(otherWord)