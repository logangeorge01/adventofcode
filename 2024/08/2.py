from collections import defaultdict

a = []

with open('input.txt') as f:
    for l in f:
        a.append(l.strip())


d = defaultdict(list)

for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j].isalnum():
            d[a[i][j]].append((i, j))

s = set()
for k, v in d.items():
    for x in range(len(v)):
        for y in range(x + 1, len(v)):
            s.add(v[x])
            s.add(v[y])

            yd = v[y][0] - v[x][0]
            xd = v[y][1] - v[x][1]

            np = (v[y][0] + yd, v[y][1] + xd)
            while 0 <= np[0] < len(a) and 0 <= np[1] < len(a[0]):
                s.add(np)
                np = (np[0] + yd, np[1] + xd)
            np = (v[x][0] - yd, v[x][1] - xd)
            while 0 <= np[0] < len(a) and 0 <= np[1] < len(a[0]):
                s.add(np)
                np = (np[0] - yd, np[1] - xd)

print(len(s))
