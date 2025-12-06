import math

a = []

with open('input.txt') as f:
    for l in f:
        ll = l.strip().split()
        if '*' not in ll: ll = [int(i) for i in ll]
        a.append(ll)

s = 0

for i in range(len(a[0])):
    l = [x[i] for x in a]
    if l[-1] == '*': s += math.prod(l[:-1])
    if l[-1] == '+': s += sum(l[:-1])

print(s)
        

