import math
def importData(data):
    """reads data file, builds list """
    ary = []
    dataset = open(data)
    for line in dataset.readlines():
        for token in line.split():
            ary.append(token)
    dataset.close()
    return ary
def parseData(ary):
    """ converts list of str to list of float"""
    gc = []
    for dub in ary:
        gc.append(float(dub))
    return gc
def calcGCContent(dna):
    """returns proportion of string that is GC"""
    gcCtr = dna.count('G') + dna.count('C')
    return gcCtr / len(dna)
def probOfMatch(gcprob, dna):
    """returns probability of random string with given GC content == dna"""
    AorT = (1-gcprob)/2
    GorC = gcprob/2
    match = 1.0
    for base in dna:
        if base == 'G' or base == 'C':
            match *= GorC
        if base == 'A' or base == 'T':
            match *= AorT
    return round(math.log10(match),3) # log10 of probability, rounded 3 spaces
l =  importData('input.txt')
s = l[0]
l.remove(l[0])
GCcont = parseData(l)
sGC = calcGCContent(s)
ans = ''
for n in GCcont:
    ans += str(probOfMatch(n, s)) + ' '
print (ans)