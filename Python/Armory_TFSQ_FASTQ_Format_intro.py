'''
Given: FASTQ file

Return: Corresponding FASTA records
'''
from _ros_utils import inFASTQ, outdata
from Bio import SeqIO

dat = inFASTQ()
q_strs = []
for seq in dat:
    q_strs.append(f'>{seq.id}\n{seq.seq}\n')
for q in q_strs:
    outdata(q)