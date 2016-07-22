def decrypt_logs(hint, message):
    # riddle two answer: fire (1230)
    # riddle three answer: rome (3210)

    # write message to text file to format
    f = open("encrypted_new.txt", "w")
    char = 0
    while char < len(message):
        f.write(message[char:char + (len(hint))] + "\n")
        char += len(hint)
    f.close()

    a1 = []

    # write text from file to array a1
    f = open("encrypted_new.txt", "r")
    for line in f:
        a1.append(list(line[:-1]))
    f.close()

    # final variable, the decoded message
    a2 = ""

    for arr in a1:
        if len(arr) < len(hint):
            if len(arr) == 1:
                arr.append(" ")
            if len(arr) == 2:
                arr.append(" ")
            if len(arr) == 3:
                arr.append(" ")
            # add lines if len(hint) > 4
        # new empty array for rearranging
        old = ["", "", "", ""]
        old[0] = arr[0]
        old[1] = arr[1]
        old[2] = arr[2]
        old[3] = arr[3]

        # allows for any hint, not just these specific ones
        arr[0] = old[int(hint[0])]
        arr[1] = old[int(hint[1])]
        arr[2] = old[int(hint[2])]
        arr[3] = old[int(hint[3])]
        # lists to strings
        arr = "".join(arr)
        a2 += arr
    return a2

check1 = decrypt_logs("3210", "e17n96o2i.C_@c4_:4n.2f2o51t7_m4o21r2n51_.")
print(check1)
print(decrypt_logs("1230", check1))