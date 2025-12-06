a = []

with open('input.txt') as f:
    for l in f:
        a.append([x for x in l.strip()])

t = 0
while True:
    s = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == '.': continue
            c = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if (k != 0 or l != 0) and 0 <= i+k < len(a) and 0 <= j+l < len(a[0]) and a[i+k][j+l] == '@':
                        c += 1
            if c < 4:
                s += 1
                a[i][j] = '.'
    if s == 0:
        print(t)
        exit(0)
    t += s


