# Script provides number of perfect matchings possible in RNA strand
# given RNA has A=U and G=C
# # of possible perfect matchings = AU! * GC!
from math import factorial
rna = 'CUUAUUCCACCACAGCGGGUUGAGCUCCCUUGUCGUAUGAAGCUCGGGAAACGUGAGGAAACGCACGUGACCAUUGUC'
AUcount = 0
GCcount = 0
for char in rna:
    if char == 'A':
        AUcount += 1
    if char == 'G':
        GCcount += 1
print( factorial(AUcount) * factorial(GCcount))