# stolen from https://github.com/mtarbit/Rosalind-Problems/blob/master/e015-lexf.py
def alpha_combs(alphabet, n, acc='', res=[]):
    if n == 0:
        res.append(acc)
    else:
        for c in alphabet:
            alpha_combs(alphabet, n - 1, acc + c, res)
    return res

large_dataset = open('input.txt').read()

bits = large_dataset.split()

alphabet = bits[:-1]
comb_len = int(bits[-1])

#alphabet.sort()
for p in alpha_combs(alphabet, comb_len):
    print p
