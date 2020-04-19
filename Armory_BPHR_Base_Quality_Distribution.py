'''
Given: FASTQ file, quality threshold q

Return: Number of positions where mean base quality falls below given threshold
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
with open('_inter.txt', 'w') as f:
    f.writelines(dat[1:])

# parse sequence file
quals = [seq.letter_annotations['phred_quality'] for seq in SeqIO.parse('_inter.txt', 'fastq')]

seq_len = len(quals[0])
num_quals = len(quals)
avg_quals = []
for i in range(seq_len):
    pos_sum = 0
    for qual in quals:
        pos_sum += qual[i]
    avg_quals.append(pos_sum/num_quals)

count = len([i for i in avg_quals if i < q])

outdata(count)