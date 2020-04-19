'''
Given: A quality threshold, along with FASTQ entries for multiple reads.

Return: The number of reads whose average quality is below the threshold.
'''

from _ros_utils import outdata
from Bio import SeqIO

# import file
dat = None
with open('_input.txt', 'r') as f:
    dat = f.read().splitlines(True)
    
# save threshold, save sequence file
threshold = int(dat[0])
with open('_inter.txt', 'w') as f:
    f.writelines(dat[1:])

# parse sequence file
low_qual = 0
for seq in SeqIO.parse('_inter.txt', 'fastq'):
    qual = seq.letter_annotations['phred_quality']
    avg = sum(qual)/len(qual)
    # find avg quality for each sequence, cound those below threshold
    if avg < threshold:
        low_qual += 1
# save count
outdata(low_qual)