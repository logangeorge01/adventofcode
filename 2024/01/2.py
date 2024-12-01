

a = []
b = []

with open('input.txt') as f:
    for l in f:
        asdf = l.split('   ')
        a.append(int(asdf[0]))
        b.append(int(asdf[1]))

s = 0
for i in range(len(a)):
    s += a[i] * b.count(a[i])

print(s)

