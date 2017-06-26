dataset = open('input.txt', 'r')
#names = [] REMOVED FOR SPEED
dnaStrings = []
# imports sequence names, dna strings, stores in separate lists
appended = False
for line in dataset:
    if line.startswith('>'):
        #names.append(line[1:].strip()) REMOVED FOR SPEED
        appended = False
    else:
        if appended is False:
            dnaStrings.append(line.strip())
            appended = True
        else:
            dnaStrings[len(dnaStrings)-1] += line.strip()
dataset.close()
# identifies shortest string of the collection
# looking for longest common motif, start with the shortest string
target = dnaStrings[0]
for s in dnaStrings:
    if len(s) < len(target):
        target = s
#block generates potential motifs
print target
motifs = []
poten = []
l = len(target)
print l
i = 800 # VALUE OF i INCREASED FOR SPEED
while i <= l: #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<COULD PROBABLY BE CHANGED TO FOR LOOP
    tl = l - i    #tl = target length, each iteration searches for shorter sub strings
    for j in range(0, l - tl):
        motF = target[j: (j + tl)]      # checks for sub strings of tl length at each position
        if motF not in poten:   #checks to make sure motif is not already present
            poten.append(motF)
# block checks each DNA string for presence of motif, adds to motif list if they are present
    com = True
    for m in poten:
        for dna in dnaStrings:
            if m in dna:
                pass
            else:
                com = False
        if com:
            motifs.append(m)
        com = True
# block prints motifs if found and stops loop, clears lists otherwise
    if not motifs:
        poten = []
    else:
        print motifs
        motifs = []
        break
    i += 1
