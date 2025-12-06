
a = []
b = []

with open('input.txt') as f:
    for l in f:
        ll = l.strip()
        if ll == '': continue
        if '-' in ll:
            a.append([int(i) for i in ll.split('-')])
            continue
        b.append(int(ll))

s = 0

for n in b:
    for aa in a:
        if n in range(aa[0], aa[1]+1):
            s += 1
            break

print(s)


