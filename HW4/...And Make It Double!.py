"""
    Author: Rachel Schreiber
	Date Created: 7/10/2016
	Assignment Code: 4-1
	Assignment Name: ...And Make It Double!
	Description:
	    Encrypt or decrypt a message using the double cipher with keyword 1 as 'fire' and keyword 2 as 'rome'
"""

def encrypt_loop(msg):
    str1 = ""
    str2 = ""
    str3 = ""
    str4 = ""
    rem = len(msg)%4
    for i in range(0, len(msg) - rem, 4):
        str1 += msg[i]
        str2 += msg[i+1]
        str3 += msg[i+2]
        str4 += msg[i+3]
    if rem >= 1:
        str1 += msg[-rem]
    if rem >= 2:
        str2 += msg[-rem]
    if rem >= 3:
        str3 += msg[-rem]

    return [str1, str2, str3, str4]

def encrypt(msg):
    newMsg = encrypt_loop(msg)
    msg = "".join(newMsg[3] + newMsg[0] + newMsg[1] + newMsg[2])
    newMsg = encrypt_loop(msg)
    msg = "".join(newMsg[3] + newMsg[2] + newMsg[1] + newMsg[0])
    return msg

def decrypt(msg):
    num1 = len(msg)//4
    rem = len(msg)%4
    num2 = num1*2
    if rem == 3:
        num2 += 1
    num3 = num2 + num1
    if rem >= 2:
        num3 += 1
    newMsg = ""
    for i in range(0, num1):
        newMsg += (msg[num3+i] + msg[num2+i] + msg[num1+i] + msg[i])
    if rem >= 1:
        newMsg += msg[-1]
    if rem >= 2:
        newMsg += msg[num3-1]
    if rem >= 3:
        newMsg += msg[num2-1]
    num2 = num1*2
    if rem >= 1:
        num2 += 1
    num3 = num2 + num1
    if rem >= 2:
        num3 += 1
    msg = ""
    for i in range(0, num1):
        msg += (newMsg[num1+i] + newMsg[num2+i] + newMsg[num3+i] + newMsg[i])
    if rem >= 1:
        msg += newMsg[num2-1]
    if rem >= 2:
        msg += newMsg[num3-1]
    if rem >= 3:
        msg += newMsg[-1]
    return msg

file = open('encrypted.txt')
choice = input("Encrypt or decrypt file: ")
line = file.readline()
while(line != ""):
    line = line[:-1]
    if choice == "decrypt":
        print(decrypt(line))
    elif choice == "encrypt":
        print(encrypt(line))
    line = file.readline()
file.close()
