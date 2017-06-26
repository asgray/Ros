import itertools
def convToList(tups):
    """produces list of strings from list of tuples"""
    l = []
    for t in tups:
        place = ''
        for char in t:
            place += char
        l.append(place)
    return l

# input from file
data = open('input.txt').read()
ins = data.split()
#letters for alphabet, number indicates max str length
alpha = ins[:-1]
comboLen = int(ins[-1])
# add _ to beginning of alphabet as dummy space
alpha.insert(0,' ')
# all permutarions of alpha, length n
unSort = convToList(itertools.product(alpha, repeat = comboLen))
#remove most of dummy space combos
sort = []
for l in alpha:
    for e in unSort:
        if e.startswith(l):
            sort.append(e)
# assemble answer in lexicographical order
ans = []
for f in sort:
    if f.find(' ', 1, -1) < 0 and f not in ans:
        ans.append(f)
# output
o = open('output.txt', 'w')
for a in ans:
    o.write(a + '\n')
o.close()

# code is slow and bad
'''input = """
D N A
3
""".strip('\n').split('\n')

alphabet, n = input[0].split(), int(input[1])

def generate(n, h=""):
    print h
    if n == 0:
        return
    for c in alphabet:
        generate(n-1, h+c)

generate(n)

def allCombos(alph, l):
    """finds all combinations of alphabet alph up to lenght l"""
    i  = 1
    temp = []
    while i <= l:
        sets = convToList(itertools.combinations(alpha, i))
        for s in sets:
            for p in convToList(itertools.product(s, repeat = i)):
                if p not in temp:
                    temp.append(p)
        i += 1
    return temp


'''