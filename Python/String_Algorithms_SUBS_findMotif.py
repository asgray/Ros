str = 'TGTACGGCGTGTACGGCCGTACGGCCCTGGGGTACGGCTTCGTACGGCGTACGGCTGGTACGGCATCCGTACGGCGCGAGTGTACGGCATGTACGGCTCGTACGGCCGGTACGGCGACCGTACGGCGGTACGGCTGAGGTACGGCGTACGGCCGGTACGGCCAGTACGGCCGTACGGCAAGTACGGCCCCTGTACGGCGTACGGCAGCGTACGGCGGTACGGCGTACGGCCGGGTACGGCGTACGGCTACGTCCCGGTACGGCGTACGGCACCAAATGACGTACGGCATGCTCGACCGTACGGCCTGTACGGCGTACGGCAGAACCGTACGGCCTGTACGGCTGTACGGCAGTACGGCGGTACGGCCTCGGGTACGGCTTGTACGGCGTACGGCTAGTACGGCTGGTACGGCGTACGGCTGTGTACGGCGTACGGCGGTACGGCTTAAGTACGGCCGTACGGCGCGCGATTTGTACGGCGGCGTACGGCGTACGGCAGTACGGCTCATGTACGGCGTAGAAGAGGCCGTTGTACGGCCTCGTACGGCAATGGGTACGGCTTAGAAGCGTACGGCCTGGTACGGCAGTACGGCGTACGGCTAGTTGTACGGCCAGAACCGGTACGGCGTACGGCGTACGGCGTACGGCGTACGGCAATGTACGGCGCTAGTACGGCATCCGCACGCAAGTACGGCGTACGGCCTACAGGTACGGCCGTACGGCGTACGGCACTTGTACGGCAGGTACGGCCCAGGGTCCCACCTGTACGGCTGGTACGGCAGTACGGCTATACGGTTTAGTACGGCGTACGGCCTAGTACGGCCGTACGGCACGTACGGCCCACTGAGTCCAGCCAGCAGTACGGCAGAGATATGAGCTGTAACGTACGGCACATGTACGGCGGTACGGC'
substr = 'GTACGGCGT'
locations = []
c = 0
l = len(substr)
for c in range(len(str)):
    if str[c] == substr[0]:
        if substr == str[c: (c+l)]:
            locations.append(c+1)
    c += 1
for loc in locations:
    print (loc)

# could use .startswith(substr