sequence = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC0'
a, c, t, g = 0, 0, 0, 0
for char in sequence:
    if char == 'A':
        a += 1
    if char == 'C':
        c += 1
    if char == 'T':
        t += 1
    if char == 'G':
        g += 1
print (a, c, g, t)
