

a = []

with open('input.txt') as f:
   for l in f:
      a.append(l.strip())

tot = 0
def rec(i):
   global tot
   cur = 0
   while i < len(a) and a[i] != '$ cd ..':
      if a[i][:4] == '$ cd':
         f, newi = rec(i + 1)
         if f <= 100000:
            tot += f
         cur += f
         i = newi
         continue
      if a[i][0].isnumeric():
         cur += int(a[i].split(' ')[0])
      i += 1
   return cur, i + 1

root, _ = rec(0)
if root <= 100000:
   tot += root

print(tot)

