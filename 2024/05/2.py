import math

a = []

with open('tests.txt') as f:
    for l in f:
        a.append([int(x) for x in l.strip().split(',')])

b = []
with open('rules.txt') as f:
    for l in f:
        b.append([int(x) for x in l.strip().split('|')])



def fix(y):
    for x in b:
        if (x[0] in y) and (x[1] in y) and (y.index(x[0])) > y.index(x[1]):
            y[y.index(x[0])], y[y.index(x[1])] = y[y.index(x[1])], y[y.index(x[0])]
            return fix(y)

s = 0
for y in a:
    p = y.copy()
    fix(y)
    if y != p:
        s += y[math.floor(len(y) / 2)]

print(s)

