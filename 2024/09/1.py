

a = []

with open('input.txt') as f:
    for l in f:
        a = [int(x) for x in l.strip()]

s = 0
c = 0
i = 0
inc = 0
bac = len(a) // 2
rev = len(a) - (2 - (len(a) % 2))
bacc = a[rev]

for i in range(len(a)):
    if i % 2 == 0:
        for j in range(a[i]):
            if i == rev and j == bacc:
                print(s)
                exit()
            s += c * inc
            c += 1
        inc += 1
        continue
    if i % 2 == 1:
        for j in range(a[i]):
            s += c * bac
            c += 1
            bacc -= 1
            if bacc == 0:
                bac -= 1
                rev -= 2
                if rev <= i:
                    print(s)
                    exit()
                bacc = a[rev]
