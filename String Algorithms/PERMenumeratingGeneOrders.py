import itertools
n = 7
set = range(1, n+1)
perms = list(itertools.permutations(set))
print len(perms)
for p in perms: print ' '.join(map(str, p))