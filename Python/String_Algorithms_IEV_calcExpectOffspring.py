#Given 6 ints corresponding to mate pairs of genotypes, assuming 2 offspring per pair, what is average number of offspring with a dominant phenotype?
AAAA = 17118
AAAa = 19939
AAaa = 16491
AaAa = 16354
Aaaa = 19477
aaaa = 17596

def findAvg(couples, offspring, proportion):
    """finds average expected of total, given proportion"""
    return couples * offspring * proportion
print (findAvg(AAAA, 2, 1) + findAvg(AAAa, 2, 1) + findAvg(AAaa, 2, 1) + findAvg(AaAa, 2, .75) + findAvg(Aaaa, 2, .5) + findAvg(aaaa, 2, 0))

"""#!/usr/bin/python
filepath = r""
displayDominant = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
offspring = 2

with open(filepath) as file:
    parentCounts = [int(x) for x in file.read().split()]

print sum([offspring * x[0] * x[1] for x in zip(displayDominant, parentCounts)])
"""