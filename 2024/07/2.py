

a = []
b = []

with open('input.txt') as f:
    for l in f:
        ll = l.strip().split(': ')
        a.append(int(ll[0]))
        b.append([int(x) for x in ll[1].split(' ')])

def opp(m, ar, i, ss, oo = ''):
    if i == len(ar):
        return m if ss == m else 0
    if ss > m:
        return 0
    if opp(m, ar, i + 1, ss + ar[i], oo + '+') > 0 or (i > 0 and opp(m, ar, i + 1, ss * ar[i], oo + '*') > 0) or opp(m, ar, i + 1, int(str(ss) + str(ar[i])), oo + '+') > 0:
        return m
    return 0

s = 0
for i in range(len(a)):
    print(i)
    s += opp(a[i], b[i], 0, 0)

print()
print(s)

