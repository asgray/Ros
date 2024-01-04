dataset = open('input.txt', 'r')
names = []
dnaStrings = []
# imports sequence names, dna strings, stores in separate lists
appended = False
for line in dataset:
    if line.startswith('>'):
        names.append(line[1:].strip())
        appended = False
    else:
        if appended is False:
            dnaStrings.append(line.strip())
            appended = True
        else:
            dnaStrings[len(dnaStrings)-1] += line.strip()
dataset.close()
n = len(dnaStrings[0])
print (len(names))
print (len(dnaStrings))
print ('dna bp = ', n)

countA = []
countC = []
countT = []
countG = []
# generates count lists for each base of necessary length
i = 0
while i < n:
    countA.append(0)
    countC.append(0)
    countT.append(0)
    countG.append(0)
    i += 1
# reads each dna string, updates count lists
for dna in dnaStrings:
    for i, c in enumerate(dna):
        if c == 'A':
            countA[i] += 1
        if c == 'C':
            countC[i] += 1
        if c == 'T':
            countT[i] += 1
        if c == 'G':
            countG[i] += 1

consensus = ''
for i in range(n):
    added = False
    aCount = countA[i]
    tCount = countT[i]
    cCount = countC[i]
    gCount = countG[i]
    l = [aCount, tCount, cCount, gCount]

    if added is False and aCount == max(l):
        consensus += 'A'
        added = True
    if added is False and tCount == max(l):
        consensus += 'T'
        added = True
    if added is False and cCount == max(l):
        consensus += 'C'
        added = True
    if added is False and gCount == max(l):
        consensus += 'G'
        added = True
print (len(consensus))
print (consensus)

print ('A:', ' '.join(map(str, countA)))
print ('C:', ' '.join(map(str, countC)))
print ('G:', ' '.join(map(str, countG)))
print ('T:', ' '.join(map(str, countT)))
print (len(countA), len(countT), len(countC), len(countG))