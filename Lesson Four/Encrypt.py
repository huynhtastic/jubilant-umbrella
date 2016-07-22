def encrypt(hint, message):
    mlen = len(message)
    num_cols = len(hint)
    cols = []
    rearranged = []
    final = ""

    for x in range(0, num_cols):
        cols.append("")
        rearranged.append("")

    a = 0
    b = 0
    while a in range(0, mlen):
        cols[b] += message[a]
        a += 1
        b += 1
        if b >= num_cols:
            b -= num_cols
    print(cols)

    for c in range(0, num_cols):
        rearranged[int(hint[c])] = cols[c]
    print(rearranged)

    for d in range(0,num_cols):
        final += rearranged[d]
    return final

encr1 = encrypt("1230", "glubglubimafish")
print(encr1)
print(encrypt("3210", encr1))