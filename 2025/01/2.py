
s = 0
c = 50

with open('input.txt') as f:
    for l in f:
        n = int(l[1:])
        cc = c + n if l[0] == 'R' else c - n

        if cc >= 100: s += cc // 100
        if cc <= 0: s += (-cc // 100) + (1 if c != 0 else 0)

        c = cc % 100

print(s)

