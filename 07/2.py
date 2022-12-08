

a = []

with open('input.txt') as f:
   for l in f:
      a.append(l.strip())

p = []
def rec(i):
   global p
   cur = 0
   while i < len(a) and a[i] != '$ cd ..':
      if a[i][:4] == '$ cd':
         f, newi = rec(i + 1)
         cur += f
         i = newi
         continue
      if a[i][0].isnumeric():
         cur += int(a[i].split(' ')[0])
      i += 1
   p.append(cur)
   return cur, i + 1

root, _ = rec(0)

num = 30000000 - (70000000 - root)
print(min(filter(lambda x: x > num, p)))

