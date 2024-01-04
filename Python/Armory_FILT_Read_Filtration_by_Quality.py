'''
Given: A quality threshold value q, percentage of bases p, and set of FASTQ entries.

Return: Number of reads in filtered FASTQ entries
'''
from _ros_utils import outdata
from Bio import SeqIO

# import file
dat = None
with open('_input.txt', 'r') as f:
    dat = f.read().splitlines(True)
    
# save threshold, save sequence file
line1 = dat[0].strip().split(' ')
q = int(line1[0])
p = int(line1[1])
with open('_inter.txt', 'w') as f:
    f.writelines(dat[1:])

# # parse sequence file
hi_qual = 0
for seq in SeqIO.parse('_inter.txt', 'fastq'):
    qual = seq.letter_annotations['phred_quality']
    count = len([i for i in qual if i >= q])
    percent = count/ len(qual)
    if count/len(qual) >= p/100:
        hi_qual += 1
# save count
outdata(hi_qual)