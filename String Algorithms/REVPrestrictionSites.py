dna = ''
dataset = open('input.txt', 'r')
#names = [] REMOVED FOR SPEED
# imports sequence names, dna strings, stores in separate lists
appended = False
for line in dataset:
    if line.startswith('>'):
        pass
        appended = False
    else:
        if appended is False:
            dna = line.strip()
            appended = True
        else:
            dna += line.strip()
dataset.close()
##########################################
def revComp(d): #*Provides reverse complement to DNA string
    rcomp = ''
    for char in d:
        if char == 'A':
            rcomp = 'T' + rcomp
        if char == 'T':
            rcomp = 'A' + rcomp
        if char == 'C':
            rcomp = 'G' + rcomp
        if char == 'G':
            rcomp = 'C' + rcomp
    return rcomp
##########################################
for index in range(0, len(dna)-1):  # test each position
    for l in range(4,14, 2):        # test each potential length
        test = dna[index: index+l]  # lengths are 4-12, evens
        if len(test) == l:          # filter for shorter strings
            halfF = test[0: l/2]
            halfB = revComp(test[l/2: l]) # identify halves of palindrome
            if halfF == halfB:      # test for palindrome
                print index+1, l
