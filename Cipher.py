import string

key="cwmfjordbankglyphsvextquiz"
alphabet = "abcdefghijklmnopqrstuvwxyz"
choice=input("Do you want to encrypt or decrypt? ")
text=input("Enter some text: ")

def encrypt(text):
    new = []
    for letter in text:
        new.append(key[alphabet.index(letter)])

    return "".join(new)
if(choice=="encrypt"):
    e = encrypt(text)
    print(e)

def decrypt(text):
    new = []
    for letter in text:
        new.append(alphabet[key.index(letter)])
    return "".join(new)
if(choice=="decrypt"):
    d=decrypt(text)
    print(d)








