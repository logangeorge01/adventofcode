

ar = []

with open('input.txt') as f:
    for l in f:
        ar.append([x for x in l.strip()])

m = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def isloop(a, i, j):
    mi = 0
    while True:
        if i == 0 or j == 0 or i == len(a) - 1 or j == len(a[0]) - 1:
            return 0
        if a[i][j] == str(mi):
            return 1
        a[i][j] = str(mi)
        while a[i + m[mi][0]][j + m[mi][1]] == '#':
            mi = (mi + 1) % 4
        i += m[mi][0]
        j += m[mi][1]

x, y = 0, 0
for i in range(len(ar)):
    for j in range(len(ar[0])):
        if ar[i][j] == '^':
            x, y = i, j
            break

s = 0
for i in range(len(ar)):
    print(i)
    for j in range(len(ar[0])):
        if ar[i][j] == '.':
            a = [x[:] for x in ar]
            a[i][j] = '#'
            s += isloop(a, x, y)


print('| ' + str(s) + ' |')

