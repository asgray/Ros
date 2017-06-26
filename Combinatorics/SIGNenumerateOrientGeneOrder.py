import itertools
def plusAndMinusPermutations(items):
    """http://stackoverflow.com/questions/10803186/list-of-all-permutations-but-without-opposite-numbers"""
    """returns permuations of a range """
    for p in itertools.permutations(items):
        for signs in itertools.product([-1,1], repeat=len(items)):
            yield [a*sign for a,sign in zip(p,signs)]
n = 2
pi = range(1, n+1)
combos = list(plusAndMinusPermutations(pi))
print len(combos)
for c in combos:
    print ' '.join(map(str,c)), '\n'