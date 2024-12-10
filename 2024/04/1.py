

a = []

with open('input.txt') as f:
    for l in f:
        a.append('x' + l.strip() + 'x')

a = ['x' * len(a[0])] + a + ['x' * len(a[0])]

def check(i, j, x, y):
    return 1 if a[i + x * 2][j + y * 2] == 'A' and a[i + x * 3][j + y * 3] == 'S' else 0

s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == 'X':
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if a[i + x][j + y] == 'M':
                        s += check(i, j, x, y)

print(s)
