a = []

with open('input.txt') as f:
    for l in f:
        a.append([x for x in l.strip()])

def rec(i, j):
    if i == len(a)-1 or j < 0 or j == len(a[0]) or a[i][j] == 'X':
        return 0
    if a[i][j] == '.':
        return rec(i+1, j)
    if a[i][j] == '^':
        a[i][j] = 'X'
        return 1 + rec(i+1, j-1) + rec(i+1, j+1)

print(rec(1, a[0].index('S')))

