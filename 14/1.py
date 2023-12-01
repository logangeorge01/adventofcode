

s = 'SCVHKHVSHPVCNBKBPVHV'

data = dict()
with open('input.txt') as f:
   for l in f:
      k, v = l.strip().split(' -> ')
      data[k] = v

for _ in range(10):
   ns = ''
   for i in range(len(s)-1):
      ns += s[i]
      if s[i:i+2] in data:
         ns += data[s[i:i+2]]
   ns += s[len(s)-1]
   s = ns

mi, ma = 10000, 0
for c in set(s):
   mi, ma = min(mi, s.count(c)), max(ma, s.count(c))

print(ma - mi)



