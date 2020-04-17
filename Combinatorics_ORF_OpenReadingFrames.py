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
def reverseComp(dna):
    """returns reverse compliment of given dna strand"""
    comp = ''
    for char in dna:
        if char == 'A':
            comp += 'T'
        if char == 'T':
            comp += 'A'
        if char == 'C':
            comp += 'G'
        if char == 'G':
            comp += 'C'
    revComp = comp[::-1]  # reverses string
    return revComp
def translate(dna):
    """returns protien string translation of DNA"""
    l = []
    codon = ''
    for bp in dna:
        codon += bp
        if len(codon) == 3:
            l.append(codon)
            codon = ''
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
    return protSeq
def transcribe(dna):
    """DNA -> RNA"""
    rna = ''
    for char in dna:
        if char == 'T':
            rna += 'U'
        else:
            rna += char
    return rna
def findORF(dna):
    """returns list of ORFs in passed DNA"""
    def findATG():
        """returns list of locations of start codon"""
        ary = []
        i = 0
        while i < len(dna):
            l = dna.find('ATG', i)
            if l == -1:
                break
            ary.append([l])
            i = l + 1
        return ary
    def findStops(start):
        """given a starrt codon in dna, finds next stop codon"""
        i = start
        stops = ['TAG', 'TGA', 'TAA']
        while i < len(dna):
            c = dna[i:i + 3]
            if c in stops:
                break
            if i >= len(dna) - 3:
                return start
            else:
                i += 3
        return i

    ORFs = findATG()
    for frame in ORFs:
        ORFs[ORFs.index(frame)].append(findStops(frame[0]))
    return ORFs

inp = importFASTA("input.txt")
inp.append(reverseComp(inp[0]))
protStr = []
for s in inp:
    locs = findORF(s)
    print(locs)
    for o in locs:
        orf = translate(transcribe(s[o[0]:o[1]]))
        if orf not in protStr and orf != '':
            protStr.append(orf)
for p in protStr:
    print (p)