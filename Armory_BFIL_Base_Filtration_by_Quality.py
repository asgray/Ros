'''
Given: FASTQ file, quality cut-off value q, Phred33 quality score assumed.

Return: FASTQ file trimmed from the both ends (removed leading and trailing bases with quality lower than q)
'''
from Bio import SeqIO
count = SeqIO.convert('_input.txt', 'fastq', '_input.fastq', 'fastq')
# converted from txt to fastq and used https://usegalaxy.org/root?tool_id=fastq_quality_trimmer

# def find_cutoff(seq, q):
#     index = 0
#     for i in range(len(seq)):
#         if seq[i] < q:
#             index = i + 1
#         else:
#             return index

# # import file
# dat = None
# with open('_input.txt', 'r') as f:
#     dat = f.read().splitlines(True)
    
# # save threshold, save sequence file
# line1 = dat[0].strip().split(' ')
# q = int(line1[0])
# with open('_inter.txt', 'w') as f:
#     f.writelines(dat[1:])

# # parse sequence file
# seqs = [seq for seq in SeqIO.parse('_inter.txt', 'fastq')]

# for seq in seqs:
#     quals = seq.letter_annotations['phred_quality']
#     forward_i = find_cutoff(quals, q)
#     reverse_i = find_cutoff(quals[::-1], q)
#     with open('_output.txt', 'a') as f:
#         SeqIO.write(seq[forward_i:-reverse_i], f, 'fastq')

