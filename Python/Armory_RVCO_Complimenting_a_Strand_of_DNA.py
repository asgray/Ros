'''
Given: A collection of n (n≤10) DNA strings.

Return: The number of given strings that match their reverse complements.
'''

from Bio import SeqIO
from _ros_utils import inFASTA, outdata

dat = inFASTA()
pals = 0
for seq in dat:
    if seq.seq == seq.seq.reverse_complement():
        pals += 1

outdata(pals)