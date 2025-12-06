
s = set()
c = []

with open('input.txt') as f:
    for l in f:
        c = [[int(i) for i in x.split('-')] for x in l.strip().split(',')]

def asdf(nn, i):
    k = len(nn) // i
    ini = nn[:k]
    for j in range(1, i):
        if nn[j*k:(j+1)*k] != ini:
            return False
    return True

for i, j in c:
    for n in range(i, j+1):
        nn = str(n)
        for k in range(2, len(nn)+1):
            if len(nn) % k == 0 and asdf(nn, k):
                s.add(n)

print(sum(s))

