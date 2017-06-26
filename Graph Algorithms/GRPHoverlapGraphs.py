''' Given a FASTA file, generate a list of segments that share
overlaps of size k.
k = 3 '''

# block opens FASTA file, adds name to list snd adds concatenated dna string to other list
dataset = open('input.txt', 'r')
names = []
dnas = []
appended = False
for line in dataset:
    if line.startswith('>'):
        names.append(line[1:].strip())
        appended = False
    else:
        if appended is False:
            dnas.append(line.strip())
            appended = True
        else:
            dnas[len(dnas) - 1] += line.strip()
dataset.close()

# block reads prefix and suffix from each dna string and stores them to separate lists. (length = 3)
pref = []
suf = []
for c in dnas:
    pref.append(c[0:3])
    suf.append(c[len(c)-3: len(c)])

# test block prints related list entries with space at the end
'''for n in names:
    print n
    print dnas[names.index(n)]
    print pref[names.index(n)], suf[names.index(n)]
    print ' '
    '''
# Output block checks for matches between suffix and prefix, and prefix and suffix, and prints corresponding
# sequence names in order
for base in names:
    for test in names:
        if base == test:
            break
        if suf[names.index(base)] == pref[names.index(test)]:
            print base, test
        if pref[names.index(base)] == suf[names.index(test)]:
            print test, base
        else:
            pass
