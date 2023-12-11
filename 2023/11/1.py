
a = []

with open('input.txt') as f:
   for l in f:
      a.append([s for s in l.strip()])

r = []
c = []

empty = ['.'] * len(a)

for i in range(len(a)):
   if a[i] == empty:
      r.append(i)
   if [a[j][i] for j in range(len(a))] == empty:
      c.append(i)

k = []

x = 0
y = 0
for i in range(len(a)):
   y = 0
   if i in r:
      x += 1
   for j in range(len(a[0])):
      if j in c:
         y += 1
      if a[i][j] == '#':
         k.append((x, y))
      y += 1
   x += 1

s = 0
for i in range(len(k)):
   for j in range(i + 1, len(k)):
      s += abs(k[j][0] - k[i][0]) + abs(k[j][1] - k[i][1])

print(s)
