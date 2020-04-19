from Bio import SeqIO 

def indata():
    file = None
    with open('_input.txt', 'r') as f:
        file = f.read()
    print('Inputs Read')
    return file

def inFASTA():
    file = list(SeqIO.parse('_input.txt', 'fasta'))
    print('FASTA File Read')
    return file

def inFASTQ():
    file = SeqIO.parse('_input.txt', 'fastq')
    print('FASTA File Read')
    return file

def outdata(out):
    out = str(out)
    with open('_output.txt', 'a') as f:
        f.write(out)
    print('Outputs Saved')

def hamming_dist(seq1, seq2):
    dH = 0
    for n in range(len(seq1)):
        if seq1[n] != seq2[n]:
            dH += 1
    return dH