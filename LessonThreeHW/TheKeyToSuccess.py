"""
    Alexandra Triampol
    7/7/16
    This code can take in strings of texts to decipher or encipher by using a dictionary.

    key = "cwm fjord bank glyphs vext quiz"
    originalABC = "abc defgh ijkl mnopqr stuv wxyz"
"""

# dictionary with the code and keys
keyCode = {
    "a": "c",
    "b": "w",
    "c": "m",
    "d": "f",
    "e": "j",
    "f": "o",
    "g": "r",
    "h": "d",
    "i": "b",
    "j": "a",
    "k": "n",
    "l": "k",
    "m": "g",
    "n": "l",
    "o": "y",
    "p": "p",
    "q": "h",
    "r": "s",
    "s": "v",
    "t": "e",
    "u": "x",
    "v": "t",
    "w": "q",
    "x": "u",
    "y": "i",
    "z": "z",
    ".": ".",
    " ": " "
       }

# make the text coded in different letters
def encipher(text, keyCode):
    encipheredCode = ""
    for stuff in text:
        encipheredCode = encipheredCode + keyCode[stuff]
    return encipheredCode


#inverts the dictionary so we don't do that by hand...again...
def invertDict(keyCode):
    newKey = {}
    for key, value in keyCode.items():
        newKey[value] = key
    return newKey


# makes the coded text normal text again
def decipher(text, keyCode):
    return encipher(text, invertDict(keyCode))


# makes user create the strings
crypticMessage = input("What's something you want to decode into normal English? " + "\n")
normalEnglish = input("What's something you want to hide with a cryptic message? "+ "\n")


# prints out the results
print("\n"+ decipher(crypticMessage,keyCode) + "\n")
print(encipher(normalEnglish,invertDict(keyCode)))