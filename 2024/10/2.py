

a = []

with open('input.txt') as f:
    for l in f:
        a.append(l.strip())

def gett(i, j, n):
    if i < 0 or i >= len(a) or j < 0 or j >= len(a[0]) or a[i][j] != n:
        return 0
    if a[i][j] == '9':
        return 1
    next = str(int(n) + 1)
    return gett(i + 1, j, next) + gett(i - 1, j, next) + gett(i, j + 1, next) + gett(i, j - 1, next)

c = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == '0':   
            c += gett(i, j, '0')

print(c)
