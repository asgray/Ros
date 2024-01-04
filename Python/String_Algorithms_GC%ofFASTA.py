dataset = open('input.txt', 'r')
d ={}
key = ''
for line in dataset:
    if line.startswith('>'):
        key = line[1:].strip()
        d[key] = ''
    else:
        d[key] += line.strip()
dataset.close()
print (d)
highID = ''
highGC = 0.0
percent = 0.0
for seq in d:
    frag = d.get(seq)
    bp = 0.0
    gc = 0.0
    for char in frag:
        bp += 1
        if char == 'C' or char == 'G':
            gc += 1
    percent = gc / bp * 100
    if percent > highGC:
        highGC = percent
        highID = seq
print(highID, highGC)
