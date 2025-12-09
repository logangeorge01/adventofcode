import heapq
import math

a = []

with open('input.txt') as f:
    for l in f:
        a.append(tuple([int(x) for x in l.strip().split(',')]))

h = []

def dist(x, y):
    return math.sqrt(sum([(x[i]-y[i])**2 for i in range(len(x))]))

for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        heapq.heappush(h, (-dist(a[i], a[j]), a[i], a[j]))
        if len(h) == (11 if len(a) == 20 else 1001):
            heapq.heappop(h)

h = sorted(h, key=lambda x:-x[0])

s = set()

for _, x, y in h:
    xx = None
    yy = None
    for g in s:
        gg = set(g)
        if x in gg:
            xx = list(g)
        if y in gg:
            yy = list(g)
    if not xx and not yy:
        s.add((x, y))
        continue
    if not xx:
        s.remove(tuple(yy))
        yy.append(x)
        s.add(tuple(yy))
        continue
    if not yy:
        s.remove(tuple(xx))
        xx.append(y)
        s.add(tuple(xx))
        continue
    if xx == yy: continue
    s.remove(tuple(xx))
    s.remove(tuple(yy))
    s.add(tuple(xx + yy))

aa = [len(t) for t in sorted(s, key=lambda x: -len(x))[:3]]
print(math.prod(aa))

