
s = 0
c = []

with open('input.txt') as f:
    for l in f:
        c = [[int(i) for i in x.split('-')] for x in l.strip().split(',')]


for i, j in c:
    for n in range(i, j+1):
        nn = str(n)
        if len(nn) % 2 == 0 and nn[:len(nn)//2] == nn[len(nn)//2:]:
            s += n

print(s)

