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
# block designates longest string as master DNA, shorter for target motif
dna = ''
subseq = ''
for s in dnaStrings:
    if len(s) > len(dna):
        dna = s
    else:
        subseq = s
# constructs a list of each position in DNA that subseq subsequences
indices = []
i = 0
for bp in range(len(dna)-1):
    if dna[bp] == subseq[i]:
        i += 1
        indices.append(bp+1)
        if i == len(subseq):
            i = 0
# constructs an answer string of len(subseq) to provide on instance of subsequence
ans = ''
for b in range(len(subseq)):
    ans += str(indices[b]) + ' '
print ans