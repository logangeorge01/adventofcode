
s = 0
c = 50

with open('input.txt') as f:
    for l in f:
        n = int(l[1:])
        c += n if l[0] == 'R' else -n
        c %= 100
        if c == 0:
            s += 1

print(s)

