def double_again(hint, message):
    # initialize some variables
    for_splicing = message
    num_cols = len(hint)
    len_cols = len(message)//len(hint)
    ex_lets = len(message)%len(hint)
    m_spliced = []
    rearranged = []
    final = ""
    # make proper number of columns
    for a in range(0, num_cols):
        m_spliced.append("x"*len_cols)
        rearranged.append("")

    # do something about length of columns
    if ex_lets > 0:
        for b in range(0, ex_lets):
            m_spliced[b] += "x"
    print(m_spliced)

    # b = 0
    # c = 0
    # while c in range(0, num_cols):
    #     e = 0
    #     while e in range(0, len(m_spliced[c])):
    #         m_spliced[c] = m_spliced[c][1:]
    #         m_spliced[c] += for_splicing[(c * len_cols): ((c + 1) * len_cols)]
    #         e += 1
    #     c += 1
    # print(m_spliced)

    # splice message and put into list indexes
    b = 0
    c = 0
    while b in range(0, num_cols):
        # m_spliced[int(hint[b])] = for_splicing[(c * len_cols): ((c + 1) * len_cols)]

        b += 1
        c += 1
    print(m_spliced)

    # # rearrange columns of m_spliced
    # for d in range(0, len(m_spliced)):
    #     rearranged[int(hint[d])] += m_spliced[d]
    # print(rearranged)

    # append extra letters

    # concatenation of list values
    f = 0
    while f <= len(hint)+1:
        for col in m_spliced:
            if len(col) > f:
                final += col[f]
        f += 1
    return(final)

check1 = double_again("3210", "fsmeiamynoellhfje")
print(check1)
print()
print(double_again("1230", check1))