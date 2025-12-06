
n = []
s = 0

with open('input.txt') as f:
    for l in f:
        n.append([int(i) for i in l.strip()])

for l in n:
    c = ''
    ci = 0
    for i in range(1, 12):
        sl = l[ci:-(12-i)]
        ci = sl.index(max(sl)) + ci
        c += str(l[ci])
        ci += 1

    c += str(max(l[ci:]))
    s += int(c)

print(s)

