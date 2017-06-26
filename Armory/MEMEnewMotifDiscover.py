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

prots = importFASTA('input.txt')
for p in prots:
    print p