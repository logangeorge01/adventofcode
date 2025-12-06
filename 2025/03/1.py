
n = []
s = 0

with open('input.txt') as f:
    for l in f:
        n.append([int(i) for i in l.strip()])

for l in n:
    mi = l.index(max(l[:-1]))
    mmi = max(l[mi+1:])
    a = l[mi]*10 + mmi
    s += a

print(s)

