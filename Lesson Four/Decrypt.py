def decrypt(hint, message):
    hlist = []
    hlist_sort = []
    mlen = len(message)
    num_cols = len(hint)
    ex_lets = len(message)%len(hint)
    cols = []
    col_lens = []
    dup_lens = []
    final = ""

    # get initial length of columns
    for a in range(0, num_cols):
        cols.append("")
        col_lens.append("")
        dup_lens.append("")
        hlist.append("")
        hlist_sort.append("")
        col_lens[a] = mlen//num_cols

    # switch hint from letters to numbers
    hlist = list(hint)
    hlist.sort()
    hlist = "".join(hlist)
    i = 0
    for letter in hint:
        hlist_sort[i] = hlist.find(letter)
        i += 1


    # make some columns longer based on if there are extra letters
    b = 0
    while ex_lets > 0:
        col_lens[b] += 1
        b += 1
        ex_lets -= 1

    # rearrange order of columns based on hint position
    for c in range(0, len(col_lens)):
        dup_lens[hlist_sort[c]] = col_lens[c]

    # fill columns from message letters
    char = 0
    for d in range(0, num_cols):
        e = 0
        while e < dup_lens[d]:
            cols[d] += message[char]
            e += 1
            char += 1

    # concatenate column indexes to final string
    g = 0
    for h in range(0, max(dup_lens)):
        for f in range(0, num_cols):
            if g in range(0, dup_lens[hlist_sort[f]]):
                final += cols[hlist_sort[f]][g]
        g += 1
    # print(final)
    return(final)

decr1 = decrypt("rome", "fsmeiamynoellhfje")
decr2 = decrypt("fire", decr1)
print(decr2)

log = open("log.txt", "a")
log.write(decr2 + "\n")
log.close()