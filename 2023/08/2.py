import math

a = {}
lr = ''

with open('input.txt') as f:
   lr = f.readline().strip()
   f.readline()
   for l in f:
      a[l[:3]] = (l[7:10], l[12:15])

e = []
for n in a:
   if n[-1:] == 'A':
      e.append(n)

i = 0
ef = [0] * len(e)
while True:
   x = 0
   for ei in range(len(e)):
      if e[ei][-1:] == 'Z':
         ef[ei] = i
         x += 1
      if lr[i % len(lr)] == 'L':
         e[ei] = a[e[ei]][0]
      else:
         e[ei] = a[e[ei]][1]
   alll = True
   for efef in ef:
      if efef == 0:
         alll = False
         break
   if alll:
      break
   i += 1

print(ef)
ans = math.lcm(*ef)
print(ans)
print(f'{ans:,}')
