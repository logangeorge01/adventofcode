import collections as cl
import copy

s = 'SCVHKHVSHPVCNBKBPVHV'

rules = dict()
count = cl.defaultdict(int)
with open('input.txt') as f:
   for l in f:
      k, v = l.strip().split(' -> ')
      rules[k] = v

for i in range(len(s)-1):
   count[s[i:i+2]] += 1

for _ in range(40):
   nc = copy.copy(count)
   for i in rules.items():
      og = nc[i[0]]
      count[i[0][0] + i[1]] += og
      count[i[1] + i[0][1]] += og
      count[i[0]] -= og


a = cl.defaultdict(int)
for i in count.items():
   a[i[0][0]] += i[1]
   a[i[0][1]] += i[1]
a[s[0]] += 1
a[s[len(s)-1]] += 1


c = [tuple(reversed(x)) for x in a.items()]
print((max(c)[0] - min(c)[0]) // 2)




