

a = []

with open('input.txt') as f:
    for l in f:
        a = [int(x) for x in l.strip()]

s = 0
c = 0
ss = ''

for i in range(len(a)):
    if i % 2 == 0:
        if a[i] % 10 == 0:
            for _ in range(a[i] // 10):
                c += 1
                ss += '.'
            continue
        for _ in range(a[i]):
            ss += str(i // 2)
            s += c * (i // 2)
            c += 1
        a[i] = -2
        continue
    if i % 2 == 1:
        sp = a[i]
        while sp > 0:
            ex = True
            for j in range(len(a) - (2 - (len(a) % 2)), -1, -2):
                if a[j] == -2 or sp == 0:
                    ex = True
                    break
                if a[j] == -1 or a[j] > sp:
                    continue
                for _ in range(a[j]):
                    ss += str(j // 2)
                    s += c * (j // 2)
                    c += 1
                sp -= a[j]
                a[j] *= 10
            if ex:
                break
        if sp > 0:
            for _ in range(sp):
                ss += str('.')
                c += 1

print(s)
