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

h = sorted(h, key=lambda x:-x[0])

s = set()
seen = set()

for _, x, y in h:
    seen.add(x)
    seen.add(y)
    if len(seen) == len(a):
        print(x[0] * y[0])
        break

