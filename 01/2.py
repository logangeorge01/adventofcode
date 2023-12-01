

a = []

with open('input.txt') as f:
   for l in f:
      a.append(l)

r = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

s = 0
for l in a:
    c1 = len(l)
    a1 = 0
    c2 = 0
    a2 = 0
    for i in range(len(l)):
        if l[i].isdigit():
            c1 = i
            a1 = int(l[c1])
            break
    for rr in r:
        if (rr in l):
            if l.index(rr) < c1:
                c1 = l.index(rr)
                a1 = r.index(rr) + 1

    for i in range(len(l)-1, -1, -1):
        if l[i].isdigit():
            c2 = i
            a2 = int(l[c2])
            break
    for rr in r:
        if (rr[::-1] in l[::-1]):
            if len(l) - len(rr) - l[::-1].index(rr[::-1]) > c2:
                c2 = len(l) - len(rr) - l[::-1].index(rr[::-1])
                a2 = r.index(rr) + 1

    c = int(str(a1) + str(a2))
    print(a1, a2, c)
    s += c

print(s)

