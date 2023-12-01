

data = []
with open('input.txt') as f:
   for l in f:
      n = l.strip().split(' -> ')
      na = []
      for i in n:
         na.append(tuple([int(x) for x in i.split(',')]))
      data.append(sorted(na))

g = [[0] * 1000 for _ in range(1000)]

for d in data:
   if d[0][0] != d[1][0] and d[0][1] != d[1][1]:
      continue

   if d[0][0] == d[1][0]:
      for i in range(d[0][1], d[1][1] + 1):
         g[i][d[0][0]] += 1
   else:
      for i in range(d[0][0], d[1][0] + 1):
         g[d[0][1]][i] += 1


ans = 0
for x in g:
   for y in x:
      if y > 1:
         ans += 1

print(ans)





