dataset = open('input.txt', 'r')
dnaStrings = []
# imports sequence names, dna strings, stores in separate lists
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
# block designates longest string as master DNA, removes from list of introns
dna = ''
for s in dnaStrings:
    if len(s) > len(dna):
        dna = s
for s in dnaStrings:
    if s == dna:
        dnaStrings.remove(s)
# block identifies the indices of introns and removes them from DNA
i =0
for s in dnaStrings:
    i = dna.find(s)
    dna = dna[0:i]+dna[i+len(s):len(dna)]
# transcribe DNA to RNA
rna = ''
for char in dna:
    if char == 'T':
        rna += 'U'
    else:
        rna += char
# split RNA into codons
l = []
codon = ''
for bp in rna:
    codon += bp
    if len(codon) == 3:
        l.append(codon)
        codon = ''
# translate RNA to protien
protSeq = ''
for cdn in l:
    if cdn[0] == 'U':
        if cdn[1] == 'C':
            protSeq += 'S'
        if cdn[1] == 'U':
            if cdn[2] == 'U' or cdn[2] == 'C':
                protSeq += 'F'
            if cdn[2] == 'A' or cdn[2] == 'G':
                protSeq += 'L'
        if cdn[1] == 'A':
            if cdn[2] == 'U' or cdn[2] == 'C':
                protSeq += 'Y'
            if cdn[2] == 'A' or cdn[2] == 'G':
                protSeq += ' '
        if cdn[1] == 'G':
            if cdn[2] == 'U' or cdn[2] == 'C':
                protSeq += 'C'
            if cdn[2] == 'G':
                protSeq += 'W'
            if cdn[2] == 'A':
                protSeq += ' '

    if cdn[0] == 'C':
        if cdn[1] == 'U':
            protSeq += 'L'
        if cdn[1] == 'C':
            protSeq += 'P'
        if cdn[1] == 'G':
            protSeq += 'R'
        if cdn[1] == 'A':
            if cdn[2] == 'U' or cdn[2] == 'C':
                protSeq += 'H'
            if cdn[2] == 'A' or cdn[2] == 'G':
                protSeq += 'Q'
    if cdn[0] == 'A':
        if cdn[1] == 'C':
            protSeq += 'T'
        if cdn[1] == 'A':
            if cdn[2] == 'U' or cdn[2] == 'C':
                protSeq += 'N'
            if cdn[2] == 'A' or cdn[2] == 'G':
                protSeq += 'K'
        if cdn[1] == 'G':
            if cdn[2] == 'U' or cdn[2] == 'C':
                protSeq += 'S'
            if cdn[2] == 'A' or cdn[2] == 'G':
                protSeq += 'R'
        if cdn[1] == 'U':
            if cdn[2] == 'U' or cdn[2] == 'C' or cdn[2] == 'A':
                protSeq += 'I'
            if cdn[2] == 'G':
                protSeq += 'M'
    if cdn[0] == 'G':
        if cdn[1] == 'U':
            protSeq += 'V'
        if cdn[1] == 'C':
            protSeq += 'A'
        if cdn[1] == 'G':
            protSeq += 'G'
        if cdn[1] == 'A':
            if cdn[2] == 'U' or cdn[2] == 'C':
                protSeq += 'D'
            if cdn[2] == 'A' or cdn[2] == 'G':
                protSeq += 'E'
print (protSeq)
