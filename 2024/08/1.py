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
            yd = v[y][0] - v[x][0]
            xd = v[y][1] - v[x][1]
            if 0 <= v[y][0] + yd < len(a) and 0 <= v[y][1] + xd < len(a[0]):
                np = (v[y][0] + yd, v[y][1] + xd)
                s.add(np)
            if 0 <= v[x][0] - yd < len(a) and 0 <= v[x][1] - xd < len(a[0]):
                np = (v[x][0] - yd, v[x][1] - xd)
                s.add(np)

print(len(s))
