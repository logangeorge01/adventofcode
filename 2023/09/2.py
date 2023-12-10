

a = []

with open('input.txt') as f:
   for l in f:
      a.append([int(n) for n in l.split(' ')])

def rec(ar):
   if ar[-2:] == [0, 0]:
      return 0
   nar = []
   for i in range(len(ar)-1):
      nar.append(ar[i+1] - ar[i])
   return ar[0] - rec(nar)

s = 0
for l in a:
   s += rec(l)

print(s)