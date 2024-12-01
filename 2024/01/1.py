

a = []
b = []

with open('input.txt') as f:
    for l in f:
        asdf = l.split('   ')
        a.append(int(asdf[0]))
        b.append(int(asdf[1]))

a = sorted(a)
b = sorted(b)

s = 0
for i in range(len(a)):
    diff = abs(a[i] - b[i])
    s += diff

print(s)

