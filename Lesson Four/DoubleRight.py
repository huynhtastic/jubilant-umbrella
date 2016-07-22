def decrypt_logs(hint, message):
    # riddle two answer: fire(1230)
    # riddle three answer: rome (3210)

    # hint is word, change to number for ordering
    # hint = list(hint)
    # print(hint)

    len_cols = len(message)//len(hint)
    num_cols = len(hint)
    spliced = []    # original encrypted message, just spliced

    for y in range(0, num_cols+1):
        spliced.append(message[(y * len_cols): (len_cols) * (y + 1)])
    print("spliced: ", spliced)

    # move extra letters to a column
    if len(message) % len(hint) > 0:
        grr = spliced.pop()
        for x in range(0, num_cols - 1):
            if len(message) % len(hint) > x:
                spliced[int(hint[x])] += grr[x]
    print("appended: ", spliced)

    rearr = spliced[0:(len(spliced))]
    # rearrange columns for message_changed concatenation
    for col in range(0, num_cols):
        rearr[col] = spliced[int(hint[col])]
    print("rearr: ", rearr)

    message_changed = ""
    i = 0
    while i <= (len_cols):
        for col in rearr:
            if len(col) > i:
                message_changed += col[i]
        i += 1
    return(message_changed)

check1 = decrypt_logs("3210", "fsmeiamynoellhfje")
print(check1)
print()
# print(decrypt_logs("1230", check1))
# print(decrypt_logs("1230", "lnifhoasfemmjlyee"))

# output after one run  lnifhoasfemmjlyee
# goal after one run    lnifhoasfemmjlyee
# output after two runs hfjloelnamyismefe
# goal after two runs   hellomynameisjeff

# real rearr for run 2  ["hoas", "femm", "jlye", "lnife"]
# goal rearr for run 2  ["hoasf", "emmj", "lyee", "lnif"]