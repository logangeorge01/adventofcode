

c = 0
a = []

with open('input.txt') as f:
   for l in f:
      a.append(int(l))

for i in range(1, len(a)):
   if a[i] > a[i-1]:
      c += 1

print(c)


