

a = []

with open('input.txt') as f:
    for l in f:
        x = l.strip()
        x = x.replace('Card   ', 'Card')
        x = x.replace('Card  ', 'Card')
        x = x.replace('Card ', 'Card')
        x = x.replace('  ', ' 0')
        a.append(x.split(' '))

s = 0
for l in a:
    w = [int(n) for n in l[1:11]]
    y = [int(n) for n in l[12:]]
    c = 0
    for i in y:
        if i in w:
            c += 1

    if c > 0:
        s += 2**(c-1)


print(s)

