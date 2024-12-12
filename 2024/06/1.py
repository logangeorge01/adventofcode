

a = []

with open('input.txt') as f:
    for l in f:
        a.append([x for x in l.strip()])

m = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def imove(i, j):
    mi = 0
    while True:
        if a[i][j] != 'X':
            a[i][j] = 'X'
        if i == 0 or j == 0 or i == len(a) - 1 or j == len(a[0]) - 1:
            return
        if a[i + m[mi][0]][j + m[mi][1]] == '#':
            mi = (mi + 1) % 4
        i += m[mi][0]
        j += m[mi][1]

def icount():
    s = 0
    for n in a:
        s += n.count('X')
    print(s)

for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == '^':
            imove(i, j)
            icount()
            exit()

