import math

a = []

with open('tests.txt') as f:
    for l in f:
        a.append([int(x) for x in l.strip().split(',')])

b = []
with open('rules.txt') as f:
    for l in f:
        b.append([int(x) for x in l.strip().split('|')])

s = 0
for y in a:
    passed = True
    for x in b:
        if (x[0] in y) and (x[1] in y) and (y.index(x[0])) > y.index(x[1]):
            passed = False
            break
    if passed:
        s += y[math.floor(len(y) / 2)]

print(s)

