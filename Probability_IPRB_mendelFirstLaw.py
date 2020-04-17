# code gives probability of random mate pair
# producing Dominant phenotype

k = 30.0
m = 20.0
n = 22.0
total = k + m + n
d = {'AA':k, 'Aa': m, 'aa': n}
ans = 0.0
print (total)
for i in d:
    for ii in d:
        if i == 'AA':
            if ii == 'AA':
                ans += (k/total)*((k-1)/(total -1))

                print ('AAAA', ans)
            if ii == 'Aa':
                ans+=(k/total)*(m/(total-1))
                print ('AAAa', ans)
            if ii == 'aa':
                ans += (k / total) * (n / (total - 1))
                print ('AAaa', ans)
        if i == 'Aa':
            if ii == 'AA':
                ans += (m / total) * (k / (total - 1))
                print ('AaAA', ans)
            if ii == 'Aa':
                ans += (m / total) * ((m-1) / (total - 1)) * 0.75
                print ('AaAa', ans)
            if ii == 'aa':
                ans += (m / total) * (n / (total - 1)) * 0.5
                print ('Aaaa', ans)
        if i == 'aa':
            if ii == 'AA':
                ans += (n / total) * (k / (total - 1))
                print ('aaAA', ans)
            if ii == 'Aa':
                ans += (n / total) * (m / (total - 1)) *0.5
                print ('aaAa', ans)
print (ans)
