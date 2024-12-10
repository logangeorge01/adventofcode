

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
        if a[i][j] == 'A':
            first = a[i + 1][j + 1] == 'M' and a[i - 1][j - 1] == 'S'
            first = first or (a[i + 1][j + 1] == 'S' and a[i - 1][j - 1] == 'M')

            sec = a[i - 1][j + 1] == 'M' and a[i + 1][j - 1] == 'S'
            sec = sec or (a[i - 1][j + 1] == 'S' and a[i + 1][j - 1] == 'M')

            if first and sec:
                s += 1
print(s)
