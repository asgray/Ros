'''
Given: A DNA string s of length at most 10 kbp, and a protein string translated by s.

Return: The index of the genetic code variant that was used for translation. (If multiple solutions exist, you may return any one.)

'''
from _ros_utils import indata, outdata
from Bio.Seq import translate
dat = indata()

dat = dat.split('\n')
dna = dat[0]
prot = dat[1]

for i in range(1,33):
    trans = translate(dna, to_stop=True, table = i)
    if trans == prot:
        outdata(str(i))
        break