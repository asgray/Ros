i = open('input.txt', 'r')
o = open('output.txt', 'w')
count = 0
for line in i:
    count += 1
    if count % 2 == 0:
        line.strip()
        o.write(line)
        print line
i.close()
o.close()
