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
        m_spliced.append("x")
        rearranged.append("")

    # do something about length of columns
    if ex_lets > 0:
        for b in range(0, ex_lets):
            m_spliced[b] += "x"
    print(m_spliced)

    d = 0
    for c in range(0,len(m_spliced)):
        m_spliced[d] = for_splicing[0:len(m_spliced[d])-1]
        for_splicing = for_splicing[len(m_spliced[d]):]
        print(m_spliced)
        print(for_splicing)
        d += 1
    print(m_spliced)

double_again("3210", "regpa")
print()
double_again("1230", "pgera")
