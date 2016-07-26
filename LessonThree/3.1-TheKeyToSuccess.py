"""
    The Key to Success

    Create code that enciphers and deciphers the message.

"c fbvcvejs bv mygblr. ylki edyvj qysedi qbkk vjj edbv qcslblr. edj nlyqkjfrj yo edj
mbpdjs qbkk wj iyxs ejve ey ckkyq pcvvcrj ey iyxs vcojei."

KEY:
'inscriptions in hollow on side of inlet puzzled professor'."

Create two methods,
"encipher" and "decipher",
that take in some text, encipher or deciphers it,
then returns the result. The deputy will then use these methods
to be able to look through the rest of the encrypted text

 This type of sentence is called a pangram. The ultimate pangram is one which is only 26 letters long,
 containing all 26 letters. This has been done, but only by using words that are so obscure that nobody
 has ever heard of them:

 Cwm fjordbank glyphs vext quiz.

 which means 'inscriptions in hollow on side of inlet puzzled professor'.
"""
#plainAlphabet = ('abcdefghijklmnopqrstuvwxyz')
#ipherAlphabet = ('cwmfjordbankglyphsvextquiz')
#plainText = ('hello')
#cipherText = ('')

from _operator import invert

cipher = {
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
    " ": " ",
    ".": "."
}


def encipher(str,cipher):
    """Given a string to encode and a substitution cipher as a dictionary, it returns the encoded string"""
    result = ""
    for x in str:
        result = result+cipher[x]
    return result

print ("Encipher of hello world:",(encipher("hello world", cipher)))
print ("Encipher of my name is:",(encipher("my name is", cipher)))

#Decoding
def decipher(str, cipher):
    return encipher(str,invert(cipher))

def invert(cipher):
    result ={}
    for key, value in cipher.items():
        result[value] = key
    return result

print ("Decipher of above:",(decipher(encipher("hello world", cipher),cipher)))
print (decipher(encipher("my name is", cipher),cipher))