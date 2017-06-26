def importFASTA(data):
    """reads FASTA file, builds list of DNA strings"""
    dnaStrings = []
    dataset = open(data)
    appended = False
    for line in dataset:
        if line.startswith('>'):
            appended = False
        else:
            if appended is False:
                dnaStrings.append(line.strip())
                appended = True
            else:
                dnaStrings[len(dnaStrings)-1] += line.strip()
    dataset.close()
    return dnaStrings
def baseMatch(s1, s2, pos):
    """checks to see if strings are the same at given position"""
    if s1[pos] == s2[pos]:
        return True
    if s1[pos] != s2[pos]:
        return False
def transitionTest(b1, b2):
    """returns True if bases passed are transitions"""
    if (b1 == 'A' and b2 == 'G') or (b1 == 'G' and b2 == 'A'):
        return True
    if (b1 == 'C' and b2 == 'T') or (b1 == 'T' and b2 == 'C'):
        return True
    else:
        return False
dnas = importFASTA('input.txt')
ition = 0.0
version = 0.0
for n in range(len(dnas[0])):               # iterate over each base
    if not baseMatch(dnas[0], dnas[1], n):  # test if bases are =
        trans = transitionTest(dnas[0][n], dnas[1][n])
        if trans:       # boolean True if transition
            ition += 1
        if not trans:   # boolean False if transversion
            version += 1
print ition / version   # print transition : transversion ratio