import math

a = []

with open('input.txt') as f:
    for l in f:
        a.append(l.strip('\n'))

s = 0
c = []
op = '' 

for i in range(len(a[0])):
    l = [x[i] for x in a]
    if len(''.join(l).strip()) == 0:
        s += sum(c) if op == '+' else math.prod(c)
        c = []
        continue
    if l[-1] != ' ': 
        op = l[-1]
    c.append(int(''.join(l[:-1])))

s += sum(c) if op == '+' else math.prod(c)

print(s)

