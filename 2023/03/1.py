
a = []
with open('input.txt') as f:
    for l in f:
        b = []
        for c in l.strip():
            b.append(c)
        a.append(b)

sym = ['@', '#', '$', '%', '&', '*', '/', '-', '=', '+']

mi = len(a)
mj = len(a[0])

def checkdim(i, j):
    return -1 < i < mi and -1 < j < mj

def checksym(i, j):
    for x in range(-1, 2):
        for y in range(-1, 2):
            if checkdim(i + x, j + y) and a[i + x][j + y] in sym:
                return True

s = ''
sm = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j].isdigit() and checksym(i, j):
            s = a[i][j]
            a[i][j] = '.'
            if checkdim(i, j-1) and a[i][j-1].isdigit():
                s = a[i][j-1] + s
                a[i][j-1] = '.'
                if checkdim(i, j-2) and a[i][j-2].isdigit():
                    s = a[i][j-2] + s
                    a[i][j-2] = '.'
            if checkdim(i, j+1) and a[i][j+1].isdigit():
                s += a[i][j+1]
                a[i][j+1] = '.'
                if checkdim(i, j+2) and a[i][j+2].isdigit():
                    s += a[i][j+2]
                    a[i][j+2] = '.'
            
            sm += int(s)


print(sm)

