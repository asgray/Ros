# for Fibonacci sequence iterated n times, with each individual only living m iterations
n = 86
m = 17

# starting pair, answer is in pairs of rabbits
babies = [0,1]
adults = [0,0]
i = 2
while i <=n:
    # babies grow up
    adults.append(babies[i-1])
    # old adults add to new adults
    adults[i] += adults[i-1]
    # remove deaths from adult population
    if i-m > 0:
        adults[i] -= babies[i-m]
    # adults make more babies
    babies.append(adults[i-1])
    i+=1
print adults[len(adults)-1] + babies[len(babies)-1]

'''416480437370410544 '''