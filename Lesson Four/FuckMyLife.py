def double_again(hint, message):
    # initialize some variables
    for_splicing = message
    num_cols = len(hint)
    init_lens = len(message)//len(hint)
    col_lens = []
    ex_lets = len(message)%len(hint)
    m_spliced = []
    rearranged = []
    final = ""

    # make proper number of columns
    for column in range(0, num_cols):
        m_spliced.append("")
        rearranged.append("")
        col_lens.append("")
        col_lens[column] = init_lens
        while ex_lets > 0:
            col_lens[column] += 1
            ex_lets -= 1
    print(col_lens)

    b = 0
    c = 0
    while b in range(0, num_cols):
        m_spliced[b] = for_splicing[c : c+col_lens[int(hint[b])]]     # [c * col_lens[int(hint[b])] : (c+1) * col_lens[int(hint[b])]]
        # print(c * col_lens[int(hint[b])], (c+1)*col_lens[int(hint[b])])

        print(b, col_lens[int(hint[b])], c, m_spliced[b])

        c += col_lens[int(hint[b])]
        b += 1
    print(m_spliced)

    # rearrange columns of lists
    for d in range(0, len(m_spliced)):
        rearranged[int(hint[d])] += m_spliced[d]
    print(rearranged)

    f = 0
    while f <= len(hint) + 1:
        for col in rearranged:
            if len(col) > f:
                final += col[f]
        f += 1
    return (final)

check1 = double_again("3210", "fsmeiamynoellhfje")
print(check1)
print()
print(double_again("1230", check1))