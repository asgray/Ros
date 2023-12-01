from itertools import product
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
def convToList(tups):
    """produces list of strings from list of tuples"""
    l = []
    for t in tups:
        place = ''
        for char in t:
            place += char
        l.append(place)
    return l
def KCombos(n):
    """returns all DNA k-mers of length k"""
    alph = ['A', 'C', 'G', 'T']
    combos = convToList(product(alph, repeat = n))
    return combos
def occurrences(string, sub):
    """returns number of subs in string, w/ overlaps"""
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count
dna = importFASTA("input.txt")  # list of dna stings
s = dna[0]                      # make dna str
k = 4                           # k = len of mer
Kmers = KCombos(k)              # generates list of ordered kmers
counts = [0]*len(Kmers)         # generates list of counts set to 0
for mer in Kmers:               # counts occurence of mer, sets count
    counts[Kmers.index(mer)] = occurrences(s, mer)

print (' '.join(str(c) for c in counts))  # prints string of counts