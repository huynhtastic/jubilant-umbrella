def decipher(key, mencoded):
    #fixed = message
    fixed = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in mencoded:
        if key.find(letter) != -1:
            fixed += alphabet[key.find(letter)]
            #fixed.replace(letter, key[key.find(letter)])
            #fixed.append(letter), alphabet[key.find(letter)])
        else:
            fixed += letter
    return fixed

def encipher(key, message):
    changed = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in message:
        if key.find(letter) != -1:
            changed += key[alphabet.find(letter)]
        else:
            changed += letter
    return changed

print(decipher("cwmfjordbunkglypzsvexhqtia", "c fbvcvejs bv mygblr. ylki edyvj qysedi qbkk vjj edbv qcslblr. edj nlyqkjfrj yo edj mbpdjs qbkk wj iyxs ejve ey ckkyq pcvvcrj ey iyxs vcojei."))
print(encipher("cwmfjordbunkglypzsvexhqtia", "a disaster is coming. only those worthy will see this warning. the knowledge of the cipher will be your test to allow passage to your safety."))