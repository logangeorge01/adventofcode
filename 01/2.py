

a = []
c = 0

with open('input.txt') as f:
   for l in f:
      a.append(int(l))

for i in range(3, len(a)):
   if a[i] > a[i-3]:
      c += 1

print(c)


