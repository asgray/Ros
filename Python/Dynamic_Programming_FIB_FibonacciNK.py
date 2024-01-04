#for Fibonacci sequence, iterated n times, by k each time
n = 6
k = 1

#total set to 1, n-1 and n-2 set to 0
total = 1
nm1, nm2 = 0, 0

i = 1
while i <= n-1:   #n-1 because n=1 set to 1 in total
    i += 1        #iterate
    nm2 = nm1 * k    #increment n
    nm1 = total
    total = nm2 + nm1  # add previous fields

print(total)
