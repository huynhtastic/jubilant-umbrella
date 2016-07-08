"""
    Author: Rachel Schreiber
	Date Created: 7/7/2016
	Assignment Code: 3-1
	Assignment Name: The Key to Success
	Description:
	    Encrypt or decrypt a message

    Key: cwmfjordbankglyphsvextquiz
    ord() -> gives ASCII for character
    chr() -> gives character based on ASCII value
    'a' = 97
"""
key = "cwmfjordbankglyphsvextquiz"

# find letter in key
def lookup(letter):
    for i in range(0, 26):
        if key[i] == letter:    # when letter found, return index
            return i

def encipher(phrase):
    encrypted = ""
    phrase = phrase.lower()  # turn phrase to all lowercase letters and punctuation
    for i in range(0, len(phrase)):
        if phrase[i] >= 'a' and phrase [i] <= 'z':  # if phrase[i] is a letter
            num = ord(phrase[i])-97  # get ASCII value and subtract value of 'a' (97) so 'a' = 0, 'b' = 1, etc.
            encrypted += key[num]   # add letter at index of key to encrypted message
        else:   # otherwise, if not letter, add directly to encrypted message
            encrypted += phrase[i]
    return encrypted

def decipher(phrase):
    decrypted = ""
    phrase = phrase.lower() # turn phrase to lower case
    for i in range(0, len(phrase)):     # for each character in phrase
        if phrase[i] >= 'a' and phrase[i] <= 'z':   # if character is letter, decipher and add to decrypted message
            num = lookup(phrase[i]) + 97
            decrypted += chr(num)
        else:   # otherwise, just add character to message
            decrypted += phrase[i]
    return decrypted

words = input("What's the phrase? ")
choice = input("encrypt or decrypt? ")
if choice == "encrypt":
    print("The encrypted message is:\n" + encipher(words))
elif choice == "decrypt":
    print("The decrypted message is:\n" + decipher(words))
else:
    print("Sorry, {0} isn't a valid choice".format(choice))