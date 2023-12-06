

a = []

with open('input.txt') as f:
    for l in f:
        x = l.strip()
        x = x.replace('Card   ', 'Card')
        x = x.replace('Card  ', 'Card')
        x = x.replace('Card ', 'Card')
        x = x.replace('  ', ' 0')
        a.append(x.split(' '))

counts = [1] * len(a)
s = 0
for li in range(len(a)):
    w = [int(n) for n in a[li][1:11]]
    y = [int(n) for n in a[li][12:]]
    c = 0
    for i in y:
        if i in w:
            c += 1

    for i in range(li+1, li+1+c):
        counts[i] += counts[li]

print(sum(counts))

